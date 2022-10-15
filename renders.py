from aiogram import types
from config import dp

import data


@dp.message_handler(commands='start')
async def Start(message: types.Message):
    user = message.chat.id
    data.Register(user)

    await message.answer('5')


def Reg(dp):
    dp.message_handler(commands=['start'])