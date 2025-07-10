# Agentic

Agentic is an AI-powered coding assistant designed to help you automate tasks, interact with Git repositories, manage files, and more. It leverages the Gemini API to understand your prompts and execute commands efficiently, while adhering to the principles of minimizing actions, prioritizing safety, and explaining steps.

## Features

- **Prompt-Based Interaction:** Interact with the assistant using natural language prompts to request actions or information. The agent is designed to understand complex prompts and respond appropriately thanks to the improved system prompt.
    *Example:* `What is the square root of 144?`
- **Code Execution:** Execute Python code snippets directly within the assistant to perform calculations, data manipulation, and other tasks.
    *Example:* `Run the following python code: print(2 + 2)`
- **Tool Usage:** Utilizes a modular tool system to extend functionality and interact with external services safely. This system ensures that all actions are performed with explicit confirmation and adhere to predefined workflow rules.
- **Chat Mode:** Engage in interactive conversations with the assistant to refine your requests and explore different options.
    *Example:* Start chat mode with `python main.py --chat`
- **Git Integration:**
  - Execute arbitrary Git commands (with confirmation for safety).
      *Example:* `Can you run git status?` The agent will explain the command and ask for confirmation before execution.
  - Generate commit messages based on code diffs.
  - Commit changes to the Git repository (requires confirmation).
  - Push branches to remote repositories (requires confirmation).
- **File System Access:**
  - List files and directories within the working directory.
      *Example:* `What files are in the current directory?`
  - Read and write file content (requires confirmation for writing).
      *Example:* `Write 'hello world' to a file named test.txt`
  - Run Python files.
      *Example:* `Run the file test.py`
- **Verbose Mode:** Get detailed information about API usage, tool execution, and other processes for debugging and understanding.
    *Example:* Enable verbose mode with `python main.py --verbose "Your prompt here"` to understand the agent's reasoning.

## Prerequisites

- Python 3.12 or higher
- A Gemini API key. You can obtain one from the Google AI Studio: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
- `uv` package manager. (See [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv) for more information.)
- A virtual environment (recommended).

## Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

    *(Replace `<repository_url>` with the actual repository URL and `<repository_name>` with the repository's directory name.)*

2.  Install dependencies using `uv`:

    ```bash
    uv sync
    ```

3.  Set the `GEMINI_API_KEY` environment variable:

    ```bash
    export GEMINI_API_KEY="YOUR_API_KEY"
    ```

    Alternatively, create a `.env` file in the project root and add the following line:

    ```
    GEMINI_API_KEY=YOUR_API_KEY
    ```

    *(The `.env` file is optional but recommended for security reasons.)*

## Usage

### Running with a Prompt

```bash
python main.py "Your prompt here"
```

Example:

```bash
python main.py "What is the square root of 144?"
```

### Chat Mode

Start the assistant in chat mode using the `--chat` flag:

```bash
python main.py --chat
```

### Verbose Mode

Enable verbose mode with the `--verbose` flag:

```bash
python main.py --verbose "Your prompt here"
```

Or in chat mode:

```bash
python main.py --chat --verbose
```

### Git Command Execution

Ask the agent to execute Git commands. The agent will explain the command and ask for confirmation before execution.

Example:

```
User: Can you run git status?
Agent: I will run git status. This will show the current status of the git repository. Are you sure you want to run: 'git status'?
```

### File System Operations

Request file system operations such as listing files, reading files, or writing to files. The agent requires confirmation before writing to files.

Example:

```
User: What files are in the current directory?
Agent: I will list files in the current directory
```

## Contributing

Contributions are welcome! Please submit a pull request with your changes. When contributing, please adhere to the core principles of minimizing actions, prioritizing safety, and explaining steps. Ensure that new tools or features are thoroughly tested to guarantee the reliability and safety of the agent. Follow these guidelines:

- Write clear and concise commit messages.
- Follow the existing code style.
- Add tests for new features.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details. (See also: [https://spdx.org/licenses/MIT.html](https://spdx.org/licenses/MIT.html))
