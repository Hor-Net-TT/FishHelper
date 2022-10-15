from aiogram import executor, types
from config import dp, bot, Admin

import renders
import renders


renders.Reg(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
