from pathlib import Path

from google.genai import types


def get_files_info(working_directory, directory=None):
    abs_working_dir = Path(working_directory).resolve()
    target_dir = abs_working_dir

    if directory:
        target_dir = target_dir / directory

    if not target_dir.is_relative_to(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not target_dir.is_dir:
        return f'Error: "{directory}" is not a directory'

    try:
        files_info = []
        for filename in target_dir.iterdir():
            filepath = target_dir / filename
            file_size = 0
            is_dir = filepath.is_dir()
            file_size = filepath.stat().st_size
            files_info.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)

    except Exception as e:
        return f"Error listing files: {e}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
