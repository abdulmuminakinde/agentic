import subprocess
from pathlib import Path

from .git_utils import check_git_repo


def git_shell_run(working_directory, command):
    message, is_git = check_git_repo(working_directory)
    if not is_git:
        return f"Error: {message}"

    abs_working_dir = Path(working_directory).resolve()
    target_dir = abs_working_dir

    if not target_dir.is_relative_to(abs_working_dir):
        return f'Error: Cannot work on "{target_dir}" as it is outside the permitted working directory'

    if not target_dir.is_dir:
        return f'Error: "{target_dir}" is not a directory'

    try:
        result = subprocess.run(
            [command],
            shell=True,
            cwd=str(target_dir),
            capture_output=True,
        )
        if result.returncode != 0:
            return f'Error: {result.stderr.decode("utf-8")}'

        return result.stdout.decode("utf-8")

    except subprocess.CalledProcessError as e:
        print(str(e))
        return f'Error: {e.stderr.decode("utf-8")}'
