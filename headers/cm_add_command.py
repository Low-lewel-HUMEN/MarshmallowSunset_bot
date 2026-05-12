import sources

from aiogram.types import Message
from aiogram.filters import Command
from aiogram.filters import CommandObject

from main_storage import dp

@dp.message(Command("add_command"))
async def add_command(message: Message, arg: CommandObject):
    await sources.internal_cm_add_command(message, arg)