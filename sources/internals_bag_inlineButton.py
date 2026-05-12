from aiogram import types
from main_storage import bot

async def internals_bag_inlineButton(callback_var: types.CallbackQuery):
    await bot.send_message(
        chat_id=callback_var.message.chat.id,
        text="You click on bag button!"
    )