from rich import print
from rich.console import Console
from rich.markdown import Markdown
from rich.padding import Padding

from config import COLOR

console = Console()


def print_formatted_response(response: str):
    try:

        markdown_response = Padding(
            Markdown(response), (1, 1), style=COLOR, expand=False
        )
        print(markdown_response)
    except Exception:
        console.print_exception(show_locals=True)
