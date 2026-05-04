import json
import main_storage

async def add_command():
    with open("access/add_command.json", "r") as file:
        _list = json.load(file)
    return _list