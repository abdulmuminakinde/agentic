import asyncio
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")


async def generate_text(prompt):
    client = genai.Client(api_key=api_key)

    response = await client.aio.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=prompt,
    )

    print(response.text)
    print(
        f"Prompt tokens: {response.usage_metadata.prompt_token_count}\n Response tokenss: {response.usage_metadata.candidates_token_count}"
    )


async def main():
    task = asyncio.create_task(
        generate_text(
            "Is cloud computing the same as cloud engineering? Reply in one paragraph maximum."
        )
    )
    print("Hello from agentic!")
    await task


if __name__ == "__main__":
    asyncio.run(main())
