from aiogram.types import Message
from aiogram.filters import CommandObject

import storage
from storage import bot

from text.cm_add_command import ERROR, LUCK, ERROR_NOT_ARG

async def add_command(message: Message, arg: CommandObject):
    if message.chat.id not in storage.access_cm_add_command:
        bot.send_message(
            chat_id=message.chat.id,
            text=ERROR
        )
        return 1

    arg_string = arg.args
    arg_array = arg_string.split()
    if len(arg_array) == 1:
        bot.send_message(
            chat_id=message.chat.id,
            text=ERROR_NOT_ARG
        )
        return 1
    
    new_command = arg_array[0]
    storage.command_list.append()
