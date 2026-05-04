from aiogram import F
from aiogram import types

from main_storage import dp
from sources.cbq_report_bag import sour_cbq__report_bag_button

@dp.callback_query(F.data == "report_bag_button")
async def cbq__report_bag_button(callback_var: types.CallbackQuery):
    await sour_cbq__report_bag_button(callback_var)