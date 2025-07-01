from google.genai import types

from core.base_tool import ToolPlugin
from functions.git_push import push_repo_to_remote, schema_push_repo_to_remote


class PushRepoToRemoteTool(ToolPlugin):
    def name(self) -> str:
        return "push_repo_to_remote"

    def schema(self) -> types.FunctionDeclaration:
        return schema_push_repo_to_remote

    def run(self, **kwargs) -> dict:
        if not kwargs.get("confirm", False):
            return {
                "status": "confirmation_required",
                "message": f"Do you want to push: '{kwargs.get('branch_name')}'?",
                "args": {**kwargs, "confirm": True},
            }

        cleaned_args = {k: v for k, v in kwargs.items() if k != "confirm"}
        result = push_repo_to_remote(**cleaned_args)
        return {
            "status": "success",
            "message": f"Pushed to origin/{kwargs.get('branch_name')}",
            "output": result,
        }
