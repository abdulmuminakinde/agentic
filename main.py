import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_function import available_functions, call_function
from prompt import system_prompt


def generate_response(
    client: genai.Client, messages: list[types.Content], verbose: bool
) -> types.GenerateContentResponse:

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt,
            ),
        )

        if verbose:
            if response.usage_metadata:
                print("Prompt tokens:", response.usage_metadata.prompt_token_count)
                print(
                    "Response tokens:", response.usage_metadata.candidates_token_count
                )
            else:
                print("No usage metadata available")

        return response

    # except genai.APIError as e:
    #     print(f"API Error: {e}")
    #     sys.exit(3)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def main():

    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    verbose = "--verbose" in sys.argv

    try:
        if not args:
            print("AI Code Assistant")
            print("\nUsage: python main.py <prompt>")
            print('Example: python main.py "3 + 5"')

        prompt = " ".join(args)
        if prompt == "":
            prompt = input("What is your prompt?\nPress Ctrl+C to exit.\n>> ")
        if prompt == "":
            print("No prompt provided. Please provide a prompt.")
            return

        client = genai.Client(api_key=api_key)

        messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]

        for iteration in range(30):

            response = generate_response(client, messages, verbose)

            if response.candidates:
                for candidate in response.candidates:
                    if candidate.content:
                        messages.append(candidate.content)

            has_function_calls = False
            has_text = False

            if response.candidates:
                for candidate in response.candidates:
                    if candidate.content and candidate.content.parts:
                        for part in candidate.content.parts:
                            if part.text:
                                print(part.text)  # Print explanatory text immediately
                                has_text = True
                            elif hasattr(part, "function_call") and part.function_call:
                                has_function_calls = True

            if response.function_calls:
                has_function_calls = True
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

            if has_function_calls:
                continue
            else:
                if not has_text:
                    if response.text:
                        print(response.text)
                print(f"\nAgent completed task in {iteration + 1} iterations.")
                break

    except KeyboardInterrupt:
        print("\nGoodbye!")
        return  # Properly exit the function on keyboard interrupt
    except Exception as e:
        print(f"Error: {e}")
        return


if __name__ == "__main__":
    main()
