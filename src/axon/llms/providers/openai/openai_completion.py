import os
from typing import Any
from pydantic import BaseModel

from axon.llms.base_llm import BaseLLM

from openai import APIConnectionError, NotFoundError, OpenAI

class OpenAICompletion(BaseLLM):
    """OpenAI completion implementation.
    This class provides direct integration with the OpenAI Python SDK,
    offering native structured outputs, streaming support.
    """
    def __init__(
        self,
        model: str = "gpt-4o",
        api_key: str | None = None,
        base_url: str | None = None,
        organization: str | None = None,
        project: str | None = None,
        timeout: float | None = None,
        max_retries: int = 2,
        default_headers: dict[str, str] | None = None,
        default_query: dict[str, Any] | None = None,
        client_params: dict[str, Any] | None = None,
        temperature: float | None = None,
        stream: bool = False,
        response_format: dict[str, Any] | type[BaseModel] | None = None,
        reasoning_effort: str | None = None,
        provider: str | None = None,
        **kwargs: Any,
    ) -> None:
        """Initialize the OpenAI completion client.
        """
        if provider is None:
            provider = kwargs.get("provider", "openai")

        self.model = model
        self.base_url = base_url
        self.organization = organization
        self.project = project
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.temperature = temperature
        self.timeout = timeout
        self.max_retries = max_retries
        self.default_headers = default_headers
        self.default_query = default_query
        self.response_format = response_format
        self.stream = stream

        super.__init__(
            model = model,
            temperature = temperature,
            api_key = self.api_key,
            base_url = base_url,
            provider = provider,
            **kwargs
        )

        self.client = OpenAI(self._get_client_params())

    def _get_client_params(self) -> dict[str, Any]:
        """Get OpenAI client parameters."""

        if self.api_key is None:
            self.api_key = os.getenv("OPENAI_API_KEY")
            if self.api_key is None:
                raise ValueError("OPENAI_API_KEY is required")

        base_params = {
            "api_key": self.api_key,
            "organization": self.organization,
            "project": self.project,
            "base_url": self.base_url            
            or os.getenv("OPENAI_BASE_URL")
            or None,
            "timeout": self.timeout,
            "max_retries": self.max_retries,
            "default_headers": self.default_headers,
            "default_query": self.default_query,
        }

        client_params = {k: v for k, v in base_params.items() if v is not None}

        if self.client_params:
            client_params.update(self.client_params)

        return client_params    