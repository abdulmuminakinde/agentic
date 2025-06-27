import subprocess
from pathlib import Path

from google.genai import types


def get_git_diff(working_directory, directory=None):
    abs_working_dir = Path(working_directory).resolve()
    target_dir = abs_working_dir

    if directory:
        target_dir = target_dir / directory

    if not target_dir.is_relative_to(abs_working_dir):
        return f'Error: Cannot work on "{directory}" as it is outside the permitted working directory'

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

        result = subprocess.check_output(
            ["git", "diff", "--no-color", "--minimal", "--cached", "-U3"],
            universal_newlines=True,
        )
        if len(result) == 0:
            return "No changes found. Did you forget to stage your changes?"
        return result

    except subprocess.CalledProcessError as e:
        return f"Error: {e}"


schema_get_git_diff = types.FunctionDeclaration(
    name="get_git_diff",
    description="Explain the git diff of the specified directory if it's in a git repository.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to get the git diff from, relative to the working directory.",
            ),
        },
    ),
)
