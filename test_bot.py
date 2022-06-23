# TODO попытка сделать домашнее задание

# 5313791416:AAGynLjrG2Jo5C0BhKiEgRPAlsjTgku-_wQ
# @try_todo_homework_bot


import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.exceptions import MessageNotModified
from aiogram.utils.callback_data import CallbackData
from os import getenv
from sys import exit
from random import randint
from contextlib import suppress
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery
# from key_boards import
from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove,
                           CallbackQuery)
from tools import DBTools

bot = Bot("5313791416:AAGynLjrG2Jo5C0BhKiEgRPAlsjTgku-_wQ")
dp = Dispatcher(bot)

user_data = {}


def get_keyboard():
    buttons = [
        types.InlineKeyboardButton(text="-1", callback_data="num_decr"),
        types.InlineKeyboardButton(text="+1", callback_data="num_incr"),
        types.InlineKeyboardButton(text="Подтвердить", callback_data="num_finish")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


async def update_num_text(message: types.Message, new_value: int):
    with suppress(MessageNotModified):
        await message.edit_text(f"Укажите число: {new_value}", reply_markup=get_keyboard())


@dp.message_handler(commands="numbers")
async def cmd_numbers(message: types.Message):
    user_data[message.from_user.id] = 0
    await message.answer("Укажите число: 0", reply_markup=get_keyboard())


@dp.callback_query_handler(Text(startswith="num_"))
async def callbacks_num(call: types.CallbackQuery):
    print(call.data)
    user_value = user_data.get(call.from_user.id, 0)
    action = call.data.split("_")[1]

    if action == "incr":
        user_data[call.from_user.id] = user_value+1
        await update_num_text(call.message, user_value+1)
    elif action == "decr":
        user_data[call.from_user.id] = user_value-1
        await update_num_text(call.message, user_value-1)
    elif action == "finish":
        await call.message.edit_text(f"Итого: {user_value}")

    await call.answer()



executor.start_polling(dp, skip_updates=True)
