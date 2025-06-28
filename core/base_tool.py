from abc import ABC, abstractmethod

from google.genai.types import FunctionDeclaration


class ToolPlugin(ABC):
    @abstractmethod
    def name(self) -> str: ...

    @abstractmethod
    def schema(self) -> FunctionDeclaration: ...

    @abstractmethod
    def run(self, **kwargs) -> dict: ...
