from models import Command, Help


class Cache:
    def __init__(self) -> None:
        self.data: dict[Command, Help] = {}

    def write(self, cmd: Command, help: Help) -> None:
        self.data[cmd] = help

    def read(self, cmd: Command) -> Help:
        return self.data[cmd]
