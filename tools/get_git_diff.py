from google.genai import types

from core.base_tool import ToolPlugin
from functions.get_git_diff import get_git_diff, schema_get_git_diff


class GetGitDiffTool(ToolPlugin):
    def name(self) -> str:
        return "get_git_diff"

    def schema(self) -> types.FunctionDeclaration:
        return schema_get_git_diff

    def run(self, **kwargs) -> dict:
        result = get_git_diff(**kwargs)
        return {"output": result}

    def requires_confirmation(self) -> bool:
        return False
