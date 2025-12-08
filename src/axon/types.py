from typing import Literal, Any
from typing_extensions import TypedDict


class LLMMessage(TypedDict):
    """Formatted LLM messages.

    """
    role: Literal["system","assistant","user"]
    content: str | list[dict[str, Any]]