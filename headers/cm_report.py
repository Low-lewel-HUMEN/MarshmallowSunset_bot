import asyncio
from aiogram.types import Message
from aiogram.filters import Command

import sources.cm_report
from storage import dp

@dp.message(Command("report"))
async def report(message: Message):
    await sources.cm_report.report(message)