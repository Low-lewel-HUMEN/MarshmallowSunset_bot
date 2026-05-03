from aiogram.types import Message
from aiogram.filters import Command

import sources.cm_help
from storage import dp

@dp.message(Command("help"))
async def help(message: Message):
    await sources.cm_help.help(message)