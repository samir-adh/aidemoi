import sys
from affogato.utils.interface import Interface
from affogato.utils.client import ClaudeClient


def main():
    client = ClaudeClient(model="claude-haiku-4-5")
    interface = Interface(client=client)
    args = sys.argv[1:]

    help = interface.seek_help(args)
    print(f"""\n{help.content}""")
    print(f"\nGenerated using {client.model}.")


if __name__ == "__main__":
    main()
