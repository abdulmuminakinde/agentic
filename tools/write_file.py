from google.genai import types

from core.base_tool import ToolPlugin
from functions.write_file import schema_write_file, write_file


class WriteFileTool(ToolPlugin):
    def name(self) -> str:
        return "write_file"

    def schema(self) -> types.FunctionDeclaration:
        return schema_write_file

    def run(self, **kwargs) -> dict:
        result = write_file(**kwargs)
        return {"output": result}

    def requires_confirmation(self) -> bool:
        return True
