from abc import ABC, abstractmethod

from typing import Any, Final

DEFAULT_CONTEXT_WINDOW_SIZE: Final[int] = 8192

class BaseLLM(ABC):
    """Abstract base class for LLM implementations.
    """

    def __init__(
        self,
        model: str,
        temperature: float | None = None,
        api_key: str | None = None,
        base_url: str | None = None,
        provider: str | None = None,
        **kwargs : Any
    ) -> None:
        """ Creates an BaseLLM instances
        Args:
            model: The model name
            temperatue: Optional model's temperature
            api_key: Model's api key
            base url: Model base url
            provider: Model provider, for instance anthropic
            kwargs: Additional provider specific parameters            
        """
        if not model:
            raise ValueError("Model name is required")

        self.model = model
        self.temperature = temperature
        self.api_key = api_key
        self.base_url = base_url
        self.provider = provider
        self.additional_parameters = kwargs

    
    @abstractmethod
    def call(
        self,
        message: str
    ) -> str:
        """Call the LLM with the given messages.

        Args:
            messages: Input messages for the LLM.
                        Can be a string or list of message dictionaries.
                        If string, it will be converted to a single user message.
                        If list, each dict must have 'role' and 'content' keys.
        Returns:
            A text response from the LLM (str)                         

        Raises:
            ValueError: If the messages format is invalid.
            TimeoutError: If the LLM request times out.
            RuntimeError: If the LLM request fails for other reasons.
        """        
