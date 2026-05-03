import asyncio
from aiogram.types import Message
from aiogram.filters import Command

import sources.cm_start
from storage import dp

@dp.message(Command("start"))
async def start(message: Message):
    await sources.cm_start.start(message)