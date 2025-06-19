import os

from google.genai import types


def write_file(working_directory, file_path, file_content):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'

    try:
        if not os.path.exists(target_file):
            os.makedirs(os.path.dirname(target_file), exist_ok=True)
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
