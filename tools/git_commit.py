from google.genai import types

from core.base_tool import ToolPlugin
from functions.git_commit import commit_git_message, schema_commit_git_message


class CommitGitMessageTool(ToolPlugin):
    def name(self) -> str:
        return "commit_git_message"

    def schema(self) -> types.FunctionDeclaration:
        return schema_commit_git_message

    def run(self, **kwargs) -> dict:
        result = commit_git_message(**kwargs)
        return {"output": result}
