from google.genai import types

from core.base_tool import ToolPlugin
from functions.git_shell_run import git_shell_run


class GitShellRunner(ToolPlugin):
    def name(self) -> str:
        return "run_git_shell_command"

    def schema(self) -> types.FunctionDeclaration:
        return types.FunctionDeclaration(
            name="run_git_shell_command",
            description="Run an arbitrary git command inside the git repo after explaining what it will do and confirming with the user. After execution, report the result of the command where necessary",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "command": types.Schema(
                        type=types.Type.STRING,
                        description="The git command to be executed inside the git repo e.g. 'git status'.",
                    ),
                    "confirm": types.Schema(
                        type=types.Type.BOOLEAN,
                        description="Must be True to execute command. If false or missing, the tool will ask for confirmation.",
                        default=False,
                    ),
                },
                required=["command"],
            ),
        )

    def run(self, **kwargs) -> dict:
        if not kwargs.get("confirm", False):
            return {
                "status": "confirmation_required",
                "message": f"Do you want to run: '{kwargs.get('command')}'?",
                "args": {**kwargs, "confirm": True},
            }

        cleaned_args = {k: v for k, v in kwargs.items() if k != "confirm"}
        result = git_shell_run(**cleaned_args)
        return {
            "status": "success",
            "message": f"Committed: {kwargs.get('message')}",
            "output": result,
        }
