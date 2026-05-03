from aiogram.types import Message
from aiogram.filters import Command

from storage import bot

from config.start_FILE_ID_animation import FILE_ID
from text.cm_start import WELCOME_TEXT

async def start(message: Message):
    await bot.send_animation(
        chat_id=message.chat.id, 
        animation=FILE_ID, 
        caption=WELCOME_TEXT
    )