from aiogram import Bot
from aiogram import Dispatcher
from config.botuk_token import BOT_TOKEN

bot = None
dp = None

# access
access_cm_add_command = None

# list
command_list = None

def init_bot():
    global bot, BOT_TOKEN, dp
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()
