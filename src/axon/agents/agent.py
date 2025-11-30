from typing import Any
from pydantic import Field, model_validator
from axon.agents.base_agent import BaseAgent
from axon.tools.base_tool import BaseTool
from axon.tasks.task import Task

class Agent(BaseAgent):

    reasoning: bool = Field(
        default=False,
        description="Whether the agent should reflect and create a plan before executing a task.",
    )

    @model_validator(mode="after")
    def init():
        """ Initializes the Agent.        
        """
        self.llm = create_llm(self.llm)


    def execute_task(
        self,
        task: Task,
        context: str | None = None,        
        tools: list[BaseTool] | None = None
    ) -> Any:
        """Execute a task.

        Args: 
            task: The task to execute
            context: Task's context
            tools: tools used by the task

        Returns:
            Tasks's execution output

        Raises
            TimeoutError: If the execution exceeds the max execution time.
            ValueError: If tasks's max execution time is not positive.
            RuntimeError: Other errors.
        """