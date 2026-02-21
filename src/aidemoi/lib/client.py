from abc import ABC, abstractmethod
from typing import Literal
import anthropic
from anthropic.types.text_block import TextBlock
from dotenv import load_dotenv


class Client(ABC):
    @abstractmethod
    def query(self, prompt: str) -> str:
        pass


load_dotenv()


class ClaudeClient(Client):
    def __init__(
        self,
        model: Literal[
            "claude-opus-4-6", "claude-sonnet-4-6", "claude-haiku-4-5"
        ] = "claude-haiku-4-5",
    ) -> None:
        self.client = anthropic.Anthropic()
        self.model = model

    def query(self, prompt: str) -> str:
        response = self.client.messages.create(
            model=self.model,
            max_tokens=1000,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        block = response.content[0]
        if not isinstance(block, TextBlock):
            raise RuntimeError("output of the model was not text")
        return block.text
