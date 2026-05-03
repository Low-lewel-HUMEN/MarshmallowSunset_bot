import asyncio
from aiogram.types import Message
from aiogram.filters import Command

from storage import bot
from storage import dp

from headers.init_report_buttons import init_report_menu

@dp.message(Command("report"))
async def report(message: Message):
    report_menu = await init_report_menu()
    await bot.send_message(
        chat_id=message.chat.id,
        text="report menu:",
        reply_markup=report_menu
    )