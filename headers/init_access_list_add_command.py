import sources.init_access_list_add_command
import storage

async def add_command_access():
    _list = await sources.init_access_list_add_command.add_command_access()
    storage.access_cm_add_command = _list
