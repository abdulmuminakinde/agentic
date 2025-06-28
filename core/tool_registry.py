from google.genai import types

from tools.get_file_content import GetFileContentTool
from tools.get_files_info import GetFilesInfoTool
from tools.get_git_diff import GetGitDiffTool
from tools.git_commit import CommitGitMessageTool
from tools.help import HelpTool
from tools.run_python_file import RunPythonFileTool
from tools.write_file import WriteFileTool

tool_plugins = [
    GetFileContentTool(),
    GetFilesInfoTool(),
    RunPythonFileTool(),
    GetGitDiffTool(),
    WriteFileTool(),
    CommitGitMessageTool(),
]

help_tool = HelpTool(tool_plugins)
tool_plugins.append(help_tool)

available_tools = types.Tool(
    function_declarations=[tool.schema() for tool in tool_plugins]
)

tool_map = {tool.name(): tool for tool in tool_plugins}
