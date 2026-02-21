import sys
from lib.interface import Interface
from lib.client import ClaudeClient


def main():
    client = ClaudeClient(model="claude-haiku-4-5")
    interface = Interface(client=client)
    args = sys.argv[1:]

    help = interface.seek_help(args)
    print(f'''\n{help.content}''')


if __name__ == "__main__":
    main()
