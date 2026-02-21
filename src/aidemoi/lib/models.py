from dataclasses import dataclass


@dataclass
class Program:
    name: str
    manual: str


@dataclass
class Command:
    program: Program
    args: list[str]


@dataclass
class Help:
    content: str
