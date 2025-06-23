# AI Code Assistant

This script provides an AI-powered code assistant that leverages the Gemini AI model to respond to user prompts, execute code, and provide solutions. It utilizes function calling to enhance its capabilities.

## Overview

The `main.py` script initializes a Gemini AI client using an API key obtained from the environment variables. It then enters a loop, processing user prompts and generating responses using the `generate_response` function. The AI model can generate text, request function calls, or both. If function calls are requested, the `call_function` function executes the corresponding function and appends the result to the message history. The loop continues until the AI model generates a final text response, which is then printed to the console.

## How it Works

1.  **Initialization:**

    - Loads environment variables, including the Gemini API key.
    - Initializes the Gemini AI client.

2.  **Prompt Processing:**

    - Takes a prompt from command-line arguments or user input.
    - Constructs a message for the AI model.

3.  **Response Generation:**

    - The `generate_response` function sends the prompt and message history to the Gemini AI model.
    - The model can respond with text, function calls, or both.

4.  **Function Calling:**

    - If the model requests a function call, the `call_function` executes the function.
    - The result of the function call is appended to the message history.

5.  **Iteration:**

    - The process repeats, with the message history growing with each turn, until the model provides a final text response.

6.  **Output:**
    - The final text response from the AI model is printed to the console.

## Usage

1.  **Set up environment variables:**

    - Create a `.env` file in the same directory as `main.py`.
    - Add your Gemini API key to the `.env` file:

      ```
      GEMINI_API_KEY=<your_gemini_api_key>
      ```

2.  **Install dependencies:**

        ```bash
        pip install -r requirements.txt
        ```

3.  **Run the script:**

    ```bash
    python main.py "<your_prompt>"
    ```

    Replace `<your_prompt>` with the prompt you want to send to the AI assistant.

    You can also run the script without a prompt and it will ask you to enter one:

    ```bash
    python main.py
    ```

4.  **Verbose Mode:**

    Add the `--verbose` flag to see more information:

    ```bash
    python main.py "<your_prompt>" --verbose
    ```

## Extending the Code

This code can be extended in several ways:

- **Adding more functions:** The `available_functions` dictionary in `call_function.py` can be extended with more functions to increase the assistant's capabilities. Each function should be defined with a clear description and parameters to allow the AI model to use it effectively.
- **Improving the prompt:** The `system_prompt` in `prompt.py` can be improved to guide the AI model's behavior and provide better responses.
- **Adding memory:** The message history is currently limited to the current session. You could add a database to store the message history and allow the assistant to remember previous interactions.
- **Implementing a user interface:** A graphical user interface (GUI) or a web interface could be added to make the assistant more user-friendly.
- **Using different models:** The script currently uses `gemini-2.0-flash-001`. You can experiment with other Gemini models to see which one works best for your needs. Make sure the model is function calling capable.

## File Structure

- `main.py`: Main script for running the AI assistant.
- `call_function.py`: Contains the `available_functions` dictionary and the `call_function` function.
- `prompt.py`: Defines the `system_prompt` used to guide the AI model.
- `requirements.txt`: Contains the list of Python packages required to run the script.
