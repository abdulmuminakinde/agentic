import asyncio
import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")


async def generate_text():
    try:
        prompt = " ".join(sys.argv[1:])
        if prompt == "":
            prompt = input("What is your prompt?\n>> ")
        if prompt == "":
            print("No prompt provided. Please provide a prompt.")
            sys.exit(1)
        suffix = " Reply in just one paragraph."
        client = genai.Client(api_key=api_key)

        messages = [
            types.Content(role="user", parts=[types.Part(text=prompt + suffix)])
        ]

        response = await client.aio.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
        )

        print(response.text)
        print(
            f"Prompt tokens: {response.usage_metadata.prompt_token_count}\n Response tokenss: {response.usage_metadata.candidates_token_count}"
        )
    except KeyboardInterrupt:
        sys.exit(0)


async def main():
    task = asyncio.create_task(generate_text())
    print("Hello from agentic!")
    await task


if __name__ == "__main__":
    asyncio.run(main())
