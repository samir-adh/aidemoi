import sys
from models import Client

def main():
    client  = Client(model="claude/opus-4.6")
    args = sys.argv[1:]

    help = client.seek_help(args)
    print(help.content)
    


if __name__ == "__main__":
    main()
