import sources.load_access
import storage.cm_accesses

async def add_command():
    _list = await sources.load_access.add_command()
    storage.cm_accesses.ACCESS_add_command = _list