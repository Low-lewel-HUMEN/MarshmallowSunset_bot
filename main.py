import sys

if __name__ == "__main__":
    print("Botuk startuping..")

else:
    print("ERROR: main not __main__")
    sys.exit()

import asyncio
import storage

# main logic
storage.init_bot()

# init list


from storage import dp
from storage import bot

# include handlers
from headers.cm_start import *
from headers.cm_help import *
from headers.cm_report import *
from headers.cbq_report_bag import *

if __name__ == "__main__":
    print("Botuk started!")
    asyncio.run(dp.start_polling(bot))
