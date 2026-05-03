import json

import storage

async def add_command_access():
    with open("access/add_command.json", "r") as file:
        _list = json.load(file)
    return _list