from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

async def get_inlineKeyboard_report_cm():
    report_menu = InlineKeyboardBuilder()
    report_menu.row(
        types.InlineKeyboardButton(
            text="I see a bag",
            callback_data="report_bag_button"
        )
    )
    report_menu.row(
        types.InlineKeyboardButton(
            text="I want to complaint on your admin",
            callback_data="report_complaint_button"
        )
    )

    return report_menu.as_markup()