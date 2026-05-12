import sources.functions_for_get_cm_accesses
import storage.cm_accesses

async def add_command():
    _list = await sources.functions_for_get_cm_accesses.add_command()
    storage.cm_accesses.ACCESS_add_command = _list