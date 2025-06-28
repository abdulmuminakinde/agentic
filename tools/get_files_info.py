from google.genai import types

from core.base_tool import ToolPlugin
from functions.get_files_info import get_files_info, schema_get_files_info


class GetFilesInfoTool(ToolPlugin):
    def name(self) -> str:
        return "get_files_info"

    def schema(self) -> types.FunctionDeclaration:
        return schema_get_files_info

    def run(self, **kwargs) -> dict:
        result = get_files_info(**kwargs)
        return {"output": result}

    def requires_confirmation(self) -> bool:
        return False
