from aiogram import F
from aiogram import types

from main_storage import dp
import sources

@dp.callback_query(F.data == "report_bag_button")
async def handler_bag_inlineButton(callback_var: types.CallbackQuery):
    await sources.internals_bag_inlineButton(callback_var)