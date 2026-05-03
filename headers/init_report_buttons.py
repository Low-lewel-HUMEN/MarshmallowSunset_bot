from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

import sources.init_report_buttons

async def init_report_menu():
    report_menu = await sources.init_report_buttons.init_report_menu()
    return report_menu