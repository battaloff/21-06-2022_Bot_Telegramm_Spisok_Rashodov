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


@dp.message_handler(commands="random")
async def cmd_random(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Нажми меня", callback_data="random_value"))
    await message.answer("Нажмите на кнопку, чтобы бот отправил число от 1 до 10", reply_markup=keyboard)


@dp.callback_query_handler(text="random_value")
async def send_random_value(call: types.CallbackQuery):
    await call.message.answer(str(randint(1, 10)))
    await call.answer(text="Спасибо, что воспользовались ботом!", show_alert=True)
    # или просто await call.answer()


executor.start_polling(dp, skip_updates=True)
