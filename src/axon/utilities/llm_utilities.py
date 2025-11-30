from typing import Any
from axon.llms.llm import LLM
from axon.llms.base_llm import BaseLLM

def create_llm(
    llm_value: str | Any | None = None
) -> LLM | BaseLLM | None:
    """Creates or returns an LLM instance based on the given llm_value.
    Args:
        llm_value: model name string, None, or an object with LLM attributes.
    Returns:
        A BaseLLM instance if successful, or None if something fails.
    """
    return LLM(
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            logprobs=logprobs,
            timeout=timeout,
            api_key=api_key,
            base_url=base_url,
            api_base=api_base,
    )