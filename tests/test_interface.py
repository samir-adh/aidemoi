from aidemoi.lib.interface import Interface


def test_client_parse():
    args = ["ls", "-a", "dir"]
    client = Interface("mock/model")
    command = client.parse(args)
    assert command.program.name == "ls"

    for arg in args[1:]:
        assert arg in command.args
