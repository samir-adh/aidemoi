import re
import subprocess

from .client import Client
from .models import Command, Help, Program
from .prompting import make_prompt


class Interface:
    def __init__(self, client: Client) -> None:
        self.client = client

    def query(self, cmd: Command) -> Help:
        command_str = cmd.program.name
        for arg in cmd.args:
            command_str += " " + arg
        prompt = make_prompt(command_str)
        response = self.client.query(prompt)
        response = response.encode().decode("unicode_escape")
        return Help(response)

    def parse(self, args: list[str]) -> Command:
        if len(args) == 0:
            raise RuntimeError("expected at least 1 command")
        program_name = args[0]
        arguments = args[1:] if len(args) > 1 else []
        manual = None
        try:
            subprocess.check_output(["man", program_name])
        except subprocess.CalledProcessError:
            pass
        program = Program(program_name, manual)

        return Command(program=program, args=arguments)

    def seek_help(self, args: list[str]) -> Help:
        command = self.parse(args)
        return self.query(command)
