from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class OpenAIAPICallRecord:
    target: str
    api_call: str
    attempts: int
    error_type: str = ""
    message: str = ""
    final_result: str = "success"
    had_error: bool = False


def format_openai_api_report(records: list[OpenAIAPICallRecord]) -> str:
    reportable = [record for record in records if record.had_error]
    if not reportable:
        return ""
    lines = ["", "## 【OpenAI API通信チェック】", ""]
    for record in reportable:
        lines.extend(
            [
                f"対象：{record.target}",
                f"API呼び出し：{'OK' if record.final_result == 'recovered' else 'NG'}",
                f"エラー種別：{record.error_type or 'なし'}",
                f"retry回数：{record.attempts}",
                f"最終結果：{record.final_result}",
                f"メッセージ：{record.message or 'なし'}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def _is_retryable_status(exc: Exception) -> bool:
    status_code = getattr(exc, "status_code", None)
    return isinstance(status_code, int) and 500 <= status_code < 600


def _sleep_seconds(attempt: int) -> float:
    return min(60.0, float(2**attempt))


def _call_with_retry(
    call: Callable[..., Any],
    *,
    api_label: str,
    stage: str,
    target: str,
    max_attempts: int,
    records: list[OpenAIAPICallRecord] | None,
    inter_attempt_sleep: Callable[[float], None] = time.sleep,
    **kwargs: Any,
) -> Any:
    from openai import APIConnectionError, APIStatusError, APITimeoutError, RateLimitError

    last_error: Exception | None = None
    had_error = False
    for attempt in range(1, max_attempts + 1):
        try:
            result = call(**kwargs)
            if had_error and records is not None:
                records.append(
                    OpenAIAPICallRecord(
                        target=target,
                        api_call=api_label,
                        attempts=attempt,
                        error_type=type(last_error).__name__ if last_error else "",
                        message=str(last_error) if last_error else "",
                        final_result="recovered",
                        had_error=True,
                    )
                )
            return result
        except (APIConnectionError, APITimeoutError, RateLimitError) as exc:
            last_error = exc
            had_error = True
            print(
                f"OpenAI API transient error during {stage}.\n"
                f"target={target}\n"
                f"attempt={attempt}/{max_attempts}\n"
                f"error={type(exc).__name__}\n"
                f"message={exc}"
            )
            if attempt < max_attempts:
                inter_attempt_sleep(_sleep_seconds(attempt))
                continue
            break
        except APIStatusError as exc:
            last_error = exc
            had_error = True
            retryable = _is_retryable_status(exc)
            level = "server" if retryable else "non-retryable status"
            print(
                f"OpenAI API {level} error during {stage}.\n"
                f"target={target}\n"
                f"attempt={attempt}/{max_attempts}\n"
                f"status={exc.status_code}\n"
                f"error={type(exc).__name__}\n"
                f"message={exc}"
            )
            if retryable and attempt < max_attempts:
                inter_attempt_sleep(_sleep_seconds(attempt))
                continue
            break
    if records is not None and last_error is not None:
        records.append(
            OpenAIAPICallRecord(
                target=target,
                api_call=api_label,
                attempts=max_attempts if _is_retryable_status(last_error) or type(last_error).__name__ in {"APIConnectionError", "APITimeoutError", "RateLimitError"} else 1,
                error_type=type(last_error).__name__,
                message=str(last_error),
                final_result="failed",
                had_error=True,
            )
        )
    if last_error is not None:
        raise last_error
    raise RuntimeError(f"OpenAI API call failed without an exception: {api_label}")


def create_response_with_retry(client: Any, *, max_attempts: int = 5, stage: str = "script_generation", target: str = "ai_assets", records: list[OpenAIAPICallRecord] | None = None, **kwargs: Any) -> Any:
    return _call_with_retry(client.responses.create, api_label="responses.create", stage=stage, target=target, max_attempts=max_attempts, records=records, **kwargs)


def generate_image_with_retry(client: Any, *, max_attempts: int = 5, stage: str = "image_generation", target: str, records: list[OpenAIAPICallRecord] | None = None, **kwargs: Any) -> Any:
    return _call_with_retry(client.images.generate, api_label="images.generate", stage=stage, target=target, max_attempts=max_attempts, records=records, **kwargs)


def edit_image_with_retry(client: Any, *, max_attempts: int = 5, stage: str = "image_generation", target: str, records: list[OpenAIAPICallRecord] | None = None, **kwargs: Any) -> Any:
    return _call_with_retry(client.images.edit, api_label="images.edit", stage=stage, target=target, max_attempts=max_attempts, records=records, **kwargs)
