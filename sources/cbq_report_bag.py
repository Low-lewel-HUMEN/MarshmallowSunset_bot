from aiogram import types
from storage import bot

async def sour_cbq__report_bag_button(callback_var: types.CallbackQuery):
    await bot.send_message(
        chat_id=callback_var.message.chat.id,
        text="You click on bag button!"
    )