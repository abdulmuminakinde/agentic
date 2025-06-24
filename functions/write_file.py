from pathlib import Path

from google.genai import types


def write_file(working_directory, file_path, file_content):
    abs_working_dir = Path(working_directory)
    target_file = abs_working_dir / file_path

    if not target_file.is_relative_to(abs_working_dir):
        return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'

    try:
        if not target_file.exists():
            target_file.parent.mkdir(parents=True, exist_ok=True)
            print(f"Created directory for file '{file_path}'")
            target_file.touch()
    except Exception as e:
        return f"Error creating directory for file '{file_path}': {e}"

    try:
        with open(target_file, "w") as file:
            file.write(file_content)
    except Exception as e:
        return f"Error writing file '{file_path}': {e}"

    return (
        f"Successfully wrote to '{file_path}' ({len(file_content)} characters written)"
    )


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes the content of a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to write to, relative to the working directory.",
            ),
            "file_content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
    ),
)
