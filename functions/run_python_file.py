import subprocess
from pathlib import Path

from google.genai import types


def run_python_file(working_directory, file_path):
    abs_working_dir = Path(working_directory).resolve()
    target_file = abs_working_dir / file_path

    if not target_file.is_relative_to(abs_working_dir):
        return f'Error: Cannot run "{file_path}" as it is outside the permitted working directory'

    if not target_file.exists():
        return f'Error: File not found: "{file_path}"'

    if not target_file.suffix == ".py":
        return f'Error: File is not a Python file: "{file_path}"'

    try:
        commands = ["python", target_file]
        result = subprocess.run(
            commands,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=working_directory,
        )
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        return "\n".join(output) if output else "No output produced"

    except Exception as e:
        return f"Error: executing Python file{file_path}: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the content of a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to run, relative to the working directory.",
            ),
        },
    ),
)
