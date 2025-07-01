import subprocess
from pathlib import Path

from google.genai import types


def push_repo_to_remote(working_directory, branch_name):
    abs_working_dir = Path(working_directory).resolve()
    target_dir = abs_working_dir

    if not target_dir.is_relative_to(abs_working_dir):
        return f'Error: Cannot work on "{target_dir}" as it is outside the permitted working directory'

    if not target_dir.is_dir:
        return f'Error: "{target_dir}" is not a directory'

    try:
        check_git_dir = subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            cwd=str(target_dir),
            capture_output=True,
            check=True,
        )
        if check_git_dir.returncode != 0:
            return f'Error: "{target_dir}" is not a git directory'

        result = subprocess.run(
            ["git", "push", "origin", branch_name],
            cwd=str(target_dir),
            capture_output=True,
        )
        if result.returncode != 0:
            return f"Error: {result.stderr.decode('utf-8')}"
    except subprocess.CalledProcessError as e:
        return str(e)

    return f"Successfully pushed {target_dir} to origin/{branch_name}"


schema_push_repo_to_remote = types.FunctionDeclaration(
    name="push_repo_to_remote",
    description="Pushes the local repo to the remote repository",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "branch_name": types.Schema(
                type=types.Type.STRING,
                description="The name of the branch to push to.",
                default="main",
            ),
            "confirm": types.Schema(
                type=types.Type.BOOLEAN,
                description="Set to true to actually push. If false or missing, the tool will ask for confirmation.",
                default=False,
            ),
        },
        required=["branch_name"],
    ),
)
