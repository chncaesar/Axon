from pydantic import (
    UUID4,
    BaseModel,
    Field,
    InstanceOf,
    Json,
    PrivateAttr,
    field_validator,
    model_validator,
)
from typing import (
    Any,
    cast,
)

from axon.agents.base_agent import BaseAgent
from axon.tasks.task import Task


class Orchestrator(BaseModel):
    name: str | None = Field(default="orchestrator")
    agents: list[BaseAgent] = Field(default_factory=list)
    tasks: list[Task] = Field(default_factory=list)
    cache: bool = Field(default=True)
    memory: bool = Field(
        default=False,
        description="If axon should use memory to store memories of it's execution",
    )
    config: Json[dict[str, Any]] | dict[str, Any] | None = Field(default=None)
    id: UUID4 = Field(default_factory=uuid.uuid4, frozen=True)

