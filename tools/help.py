from google.genai import types

from core.base_tool import ToolPlugin


class HelpTool(ToolPlugin):
    def __init__(self, tools):
        self._tools = tools

    def name(self) -> str:
        return "help"

    def schema(self) -> types.FunctionDeclaration:
        return types.FunctionDeclaration(
            name="help",
            description="List all available tools the assistant can call, along with descriptions.",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={},
            ),
        )

    def run(self, **kwargs):
        tool_list = [
            {
                "name": tool.name(),
                "description": tool.schema().description or "No description",
            }
            for tool in self._tools
            if callable(getattr(tool, "schema", None))
        ]

        if not tool_list:
            return {"output": "No tools registered."}

        return {"tools": tool_list}

    def requires_confirmation(self) -> bool:
        return False
