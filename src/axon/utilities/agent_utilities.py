from axon.utilities.exceptions.context_window_exceeding_exception import LLMContextLengthExceededError

def is_context_length_exceeded(exception: Exception) -> bool:
    """Check if the exception is due to context length exceeding.

    Args:
        exception: The exception to check

    Returns:
        bool: True if the exception is due to context length exceeding
    """
    return LLMContextLengthExceededError(str(exception))._is_context_limit_error(
        str(exception)
    )