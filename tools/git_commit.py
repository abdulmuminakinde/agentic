from google.genai import types

from core.base_tool import ToolPlugin
from functions.git_commit import commit_git_message, schema_commit_git_message


class CommitGitMessageTool(ToolPlugin):
    def name(self) -> str:
        return "commit_git_message"

    def schema(self) -> types.FunctionDeclaration:
        return schema_commit_git_message

    def run(self, **kwargs) -> dict:
        if not kwargs.get("confirm", False):
            return {
                "status": "confirmation_required",
                "message": f"Do you want to commit: '{kwargs.get('message')}'?",
                "args": {**kwargs, "confirm": True},
            }

        cleaned_args = {k: v for k, v in kwargs.items() if k != "confirm"}
        result = commit_git_message(**cleaned_args)
        return {
            "status": "success",
            "message": f"Committed: {kwargs.get('message')}",
            "output": result,
        }
