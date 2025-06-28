from google.genai import types

from core.base_tool import ToolPlugin
from functions.run_python_file import run_python_file, schema_run_python_file


class RunPythonFileTool(ToolPlugin):
    def name(self) -> str:
        return "run_python_file"

    def schema(self) -> types.FunctionDeclaration:
        return schema_run_python_file

    def run(self, **kwargs) -> dict:
        result = run_python_file(**kwargs)
        return {"output": result}

    def requires_confirmation(self) -> bool:
        return False
