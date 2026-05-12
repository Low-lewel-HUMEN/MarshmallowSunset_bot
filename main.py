import sys

if __name__ == "__main__":
    print("Botuk startuping..")

else:
    print("ERROR: main not __main__")
    sys.exit()

import asyncio
import main_storage

# main logic
main_storage.init_bot()

# init list


from main_storage import dp
from main_storage import bot

# include handlers
from headers.cm_start import *
from headers.cm_help import *
from headers.cm_report import *
from headers.handler_bag_inlineButton import *

if __name__ == "__main__":
    print("Botuk started!")
    asyncio.run(dp.start_polling(bot))
