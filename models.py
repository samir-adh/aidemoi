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


class Client:
    def __init__(self, model: str) -> None:
        self.model = model

    def query(self, cmd: Command) -> Help:
        return Help(f"this is a help message for running `{cmd.program.name} {cmd.args}`.\n")

    def parse(self, args: list[str]) -> Command:
        if len(args) == 0:
            raise RuntimeError("expected at least 1 command")
        program_name = args[0]
        arguments = args[1:] if len(args) > 1 else []
        program = Program(program_name, "")
        return Command(program=program, args=arguments)

    def seek_help(self, args: list[str]) -> Help:
        command = self.parse(args)
        return self.query(command)

class Cache:
    def __init__(self) -> None:
        self.data: dict[Command, Help] = {}

    def write(self, cmd: Command, help: Help) -> None:
        self.data[cmd] = help

    def read(self, cmd: Command) -> Help:
        return self.data[cmd]


    