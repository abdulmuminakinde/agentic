from google.genai import types

from config import WORKING_DIR
from core.tool_registry import tool_map


def call_function(function_call_part, verbose=False):
    function_name = function_call_part.name
    args = dict(function_call_part.args)
    args["working_directory"] = WORKING_DIR

    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_name}")

    tool = tool_map.get(function_name)
    if not tool:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )

    try:
        result = tool.run(**args)
        if not result:
            result = {"output": "No tools found or response was empty."}
    except Exception as e:
        result = {"error": str(e)}

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response=result,
            )
        ],
    )
