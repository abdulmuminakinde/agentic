# Agentic

This project is an AI-powered code assistant that uses the Gemini API to respond to user prompts, execute code, and perform various tasks. It's designed with a modular architecture that allows for easy extension with new tools.

## Features

- **Prompt-based interaction:** You can provide a prompt to the assistant, and it will generate a response based on the prompt.
- **Code execution:** The assistant can execute Python code snippets.
- **Function calling:** The assistant can call predefined functions to perform specific tasks.
- **Chat mode:** An interactive chat mode allows you to have a conversation with the assistant.
- **Code review assistance:** The assistant can analyze git diffs to provide insights and suggestions for code improvements.
- **Commit git changes:** Commits changes to the git repository with a specified message.
- **Verbose mode:** Provides detailed information about the API usage and function call results.

## Prerequisites

- Python 3.12 or higher
- A Gemini API key

## Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2.  Install the dependencies:

    ```bash
    uv sync
    ```

3.  Set the `GEMINI_API_KEY` environment variable:

    ```bash
    export GEMINI_API_KEY="YOUR_API_KEY"
    ```

    You can also set this in a `.env` file in the project root.

## Usage

### Running with a prompt

```bash
python main.py "Your prompt here"
```

Example:

```bash
python main.py "3 + 5"
```

### Chat mode

To start the assistant in chat mode, use the `--chat` flag:

```bash
python main.py --chat
```

### Verbose mode

To enable verbose mode, use the `--verbose` flag:

```bash
python main.py --verbose "Your prompt here"
```

or in chat mode:

```bash
python main.py --chat --verbose
```

## Contributing

Contributions are welcome! Please submit a pull request with your changes.

