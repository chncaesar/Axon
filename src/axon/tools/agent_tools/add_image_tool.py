from pydantic import BaseModel, Field

from axon.tools import BaseTool

TOOL_NAME = "Add Image"
TOOL_DESCRIPTION = "Tool for adding images to the content"
    

class AddImageToolSchema(BaseModel):
    image_url: str = Field(..., description="The URL or path of the image to add")
    desc: str | None = Field(
        default=None, description="Optional context or question about the image"
    )


class AddImageTool(BaseTool):
    """Tool for adding images to the content"""

    name: str = Field(default=TOOL_NAME)
    description: str = Field(default=TOOL_DESCRIPTION)
    args_schema: type[BaseModel] = AddImageToolSchema

    def _run(
        self,
        image_url: str,
        desc: str | None = None,
        **kwargs,
    ) -> dict:
        desc = desc or "Add the image to content"
        content = [
            {"type": "text", "text": desc},
            {
                "type": "image_url",
                "image_url": {
                    "url": image_url,
                },
            },
        ]

        return {"role": "user", "content": content}
