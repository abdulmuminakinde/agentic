from google.genai import types

from core.base_tool import ToolPlugin
from functions.get_files_content import get_file_content, schema_get_file_content


class GetFileContentTool(ToolPlugin):
    def name(self) -> str:
        return "get_file_content"

    def schema(self) -> types.FunctionDeclaration:
        return schema_get_file_content

    def run(self, **kwargs) -> dict:
        result = get_file_content(**kwargs)
        return {"output": result}
