from aiogram.types import Message
from aiogram.filters import Command

from storage import bot
from storage import dp

from texts.cm_help import HELP_TEXT

@dp.message(Command("help"))
async def help(message: Message):
    await bot.send_message(
        chat_id=message.chat.id, 
        text=HELP_TEXT
    )