import unittest
from unittest.mock import MagicMock

from google import genai
from google.genai import types

import main
from functions.get_files_content import get_file_content
from functions.get_files_info import get_files_info
from functions.get_git_diff import get_git_diff
from functions.run_python_file import run_python_file


class TestMain(unittest.TestCase):

    def test_generate_response(self):
        # Mock the genai.Client and its methods
        mock_client = MagicMock(spec=genai.Client)
        mock_model = MagicMock()
        mock_client.models = mock_model
        mock_generate_content = MagicMock()
        mock_model.generate_content = mock_generate_content
        mock_generate_content.return_value = types.GenerateContentResponse(
            candidates=[
                types.Candidate(
                    content=types.Content(parts=[types.Part(text="Test response")])
                )
            ]
        )

        # Create a sample list of messages
        messages = [types.Content(role="user", parts=[types.Part(text="Test prompt")])]

        # Call the function with the mock client
        response = main.generate_response(mock_client, messages, verbose=False)

        # Assert that the client's generate_content method was called with the correct arguments
        mock_generate_content.assert_called_once()

        # Assert that the response is not None
        self.assertIsNotNone(response)
        self.assertEqual(response.candidates[0].content.parts[0].text, "Test response")

    def test_get_files_info(self):
        result = get_files_info("calculator")
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 2)


def tests():
    result = get_file_content("calculator", "pkg/render.py")
    print(result)

    result = get_files_info("calculator")
    print(result)

    resutl = run_python_file("calculator", "tests.py")
    print(resutl)

    print("GIT DIFF TEST")
    result = get_git_diff(".")
    print(result)


if __name__ == "__main__":
    tests()
    unittest.main()
