import json

async def add_command():
    with open("access/add_command.json", "r") as file:
        cm_used_accesses_list = json.load(file)
    return cm_used_accesses_list