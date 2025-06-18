import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_function import available_functions
from config import system_prompt


def generate_text(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt,
        ),
    )

    if verbose:
        print(
            f"Prompt tokens: {response.usage_metadata.prompt_token_count}\n Response tokenss: {response.usage_metadata.candidates_token_count}"
        )

    if response.function_calls:
        for function_call in response.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print(response.text)


def main():

    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    try:
        verbose = "--verbose" in sys.argv
        args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

        if not args:
            print("AI Code Assistant")
            print("\nUsage: python main.py <prompt>")
            print('Example: python main.py "3 + 5"')

        prompt = " ".join(args)
        if prompt == "":
            prompt = input("What is your prompt?\nPress Ctrl+C to exit.\n>> ")
        if prompt == "":
            print("No prompt provided. Please provide a prompt.")
            sys.exit(1)
        client = genai.Client(api_key=api_key)

        messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]

        generate_text(client, messages, verbose)
    except KeyboardInterrupt:
        print("\nGoodbye!")


if __name__ == "__main__":
    main()
