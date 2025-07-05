import subprocess
from pathlib import Path


def check_git_repo(directory) -> tuple[str, bool]:
    abs_working_dir = Path(directory).resolve()
    target_dir = abs_working_dir

    if not target_dir.is_relative_to(abs_working_dir):
        return (
            f'Error: Cannot work on "{target_dir}" as it is outside the permitted working directory',
            False,
        )

    if not target_dir.is_dir():
        return f'Error: "{target_dir}" is not a directory', False

    try:
        check_git_dir = subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            cwd=str(target_dir),
            capture_output=True,
            check=True,
        )
        if check_git_dir.returncode != 0:
            return f'Error: "{target_dir}" is not a git directory', False
    except subprocess.CalledProcessError as e:
        return f"Error: {str(e)}", False

    return f'Success: "{target_dir}" is a git directory', True
