import sources.cm_add_command

from aiogram.types import Message
from aiogram.filters import Command
from aiogram.filters import CommandObject

from storage import dp

@dp.message(Command("add_command"))
async def add_command(message: Message, arg: CommandObject):
    await sources.cm_add_command.add_command(message, arg)