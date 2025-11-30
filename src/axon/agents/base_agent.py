
from pydantic import (
    BaseModel,
    Field,
    UUID4,
)
import uuid
from typing import Any
from abc import ABC, abstractmethod
from axon.tools.base_tool import BaseTool
from axon.llms.llm import LLM
from axon.tasks.task import Task


class BaseAgent(BaseModel, ABC):
    uuid: UUID4 = Field(default_factory=uuid.uuid4, frozen=True)
    name: str = Field()
    llm: LLM = Field()
    task: Task = Field()
    background: str = Field(description="Background of the agent")
    config: dict[str, Any] | None = Field(
        description="Configuration for the agent", default=None, exclude=True
    )

    @abstractmethod
    def execute_task(
        self,
        task: Any,
        context: str | None = None,
        tools: list[BaseTool] | None = None,
    ) -> str:
        pass