import asyncio
from aiogram.types import Message
from aiogram.filters import Command

from storage import bot
from storage import dp

from config.start_FILE_ID_animation import FILE_ID
from texts.cm_start import WELCOME_TEXT

@dp.message(Command("start"))
async def start(message: Message):
    await bot.send_animation(
        chat_id=message.chat.id, 
        animation=FILE_ID, 
        caption=WELCOME_TEXT
    )