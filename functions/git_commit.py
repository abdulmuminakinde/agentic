import subprocess
from pathlib import Path

from google.genai import types


def commit_git_message(working_directory, message):
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
            ["git", "commit", "-m", message],
            cwd=str(target_dir),
            capture_output=True,
        )
        if result.returncode != 0:
            return f'Error: {result.stderr.decode("utf-8")}'

    except subprocess.CalledProcessError as e:
        print(str(e))
        return f'Error: {e.stderr.decode("utf-8")}'

    return f'Commit successful: "{message}"'


schema_commit_git_message = types.FunctionDeclaration(
    name="commit_git_message",
    description="Commit git changes with the specified message. Requires confirmation before execution.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "message": types.Schema(
                type=types.Type.STRING,
                description="The commit message to be committed inside the git repo.",
            ),
            "confirm": types.Schema(
                type=types.Type.BOOLEAN,
                description="Set to true to actually commit. If false or missing, the tool will ask for confirmation.",
                default=False,
            ),
        },
        required=["message"],
    ),
)
