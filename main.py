import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompt_toolkit import PromptSession
from rich.console import Console

from core.function_dispatcher import call_function
from core.tool_registry import available_tools
from format import print_formatted_response
from prompt import system_prompt


def generate_response(
    client: genai.Client, messages: list[types.Content], verbose: bool
) -> types.GenerateContentResponse:

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_tools],
                system_instruction=system_prompt,
            ),
        )

        if verbose:
            if response.usage_metadata:
                print("Prompt tokens:", response.usage_metadata.prompt_token_count)
                print(
                    "Response tokens:",
                    response.usage_metadata.candidates_token_count,
                )
            else:
                print("No usage metadata available")

        return response

    # except genai.APIError as e:
    #     print(f"API Error: {e}")
    #     sys.exit(3)

    except Exception:
        with open("log.txt", "w") as f:
            console = Console(file=f)
            console.print_exception()
        sys.exit(1)


_conversation_history = []


def chat_with_agent(
    client: genai.Client,
    session: PromptSession,
    verbose: bool = False,
):
    global _conversation_history
    messages = _conversation_history
    while True:
        prompt = session.prompt(">> ")

        if prompt == "":
            continue

        if prompt.lower() == "exit":
            break

        messages.append(types.Content(role="user", parts=[types.Part(text=prompt)]))

        try:
            for _ in range(30):
                response = generate_response(client, messages, verbose)

                if response.candidates:
                    for candidate in response.candidates:
                        if candidate.content:
                            messages.append(candidate.content)

                if response.candidates and response.candidates[0].content:
                    for part in response.candidates[0].content.parts or []:
                        if part.text:
                            print_formatted_response(part.text)

                if response.function_calls:

                    tool_turn_parts = []
                    for function_call_part in response.function_calls:
                        result = call_function(function_call_part, verbose)

                        if not result.parts or not result.parts[0].function_response:
                            raise Exception(
                                "Empty function call results or invalid function response"
                            )
                        if verbose:
                            print(f"-> {result.parts[0].function_response.response}")
                        tool_turn_parts.append(result.parts[0])

                    if tool_turn_parts:
                        messages.append(
                            types.Content(role="tool", parts=tool_turn_parts)
                        )
                        continue

                    messages.append(types.Content(role="tool", parts=tool_turn_parts))
                    continue
                else:
                    break
        except Exception:
            console = Console()
            console.print_exception()
            break


def main():
    load_dotenv()
    session = PromptSession(vi_mode=True)

    api_key = os.getenv("GEMINI_API_KEY")

    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    verbose = "--verbose" in sys.argv
    chat = "--chat" in sys.argv

    try:
        client = genai.Client(api_key=api_key)
        if not args:
            print("AI Code Assistant")
            print("\nUsage: python main.py <prompt>")
            print('Example: python main.py "3 + 5"')
            if chat:
                chat_with_agent(client, session, verbose=verbose)
                return
            prompt = session.prompt("What is your prompt?\nPress Ctrl+C to exit.\n>> ")
        else:
            prompt = " ".join(args)

        if prompt == "":
            print("No prompt provided. Please provide a prompt.")
            return

        messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]

        for _ in range(30):
            response = generate_response(client, messages, verbose)

            if response.candidates:
                for candidate in response.candidates:
                    if candidate.content:
                        messages.append(candidate.content)

            if response.candidates and response.candidates[0].content:
                for part in response.candidates[0].content.parts or []:
                    if part.text:
                        print(part.text)

            if response.function_calls:
                for function_call_part in response.function_calls:
                    function_call_result = call_function(function_call_part, verbose)
                    if (
                        not function_call_result.parts
                        or not function_call_result.parts[0].function_response
                    ):
                        raise Exception("empty function call result")
                    if verbose:
                        print(
                            f"-> {function_call_result.parts[0].function_response.response}"
                        )
                    messages.append(function_call_result)
                    continue
            else:
                break

    except KeyboardInterrupt:
        print("\nGoodbye!")
        return  # Properly exit the function on keyboard interrupt


if __name__ == "__main__":
    main()
