from aiogram.types import Message

from main_storage import bot

from text.cm_help import HELP_TEXT

async def help(message: Message):
    await bot.send_message(
        chat_id=message.chat.id, 
        text=HELP_TEXT
    )