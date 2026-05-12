from aiogram.types import Message

from main_storage import bot

from headers.get_inlineKeyboard_report_cm import get_inlineKeyboard_report_cm

async def report(message: Message):
    report_menu = await get_inlineKeyboard_report_cm()
    await bot.send_message(
        chat_id=message.chat.id,
        text="report menu:",
        reply_markup=report_menu
    )