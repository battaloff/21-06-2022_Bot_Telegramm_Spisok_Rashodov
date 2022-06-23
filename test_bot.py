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





@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Доходы", "Расходы"]
    keyboard.add(*buttons)
    await message.answer("Сделайте свой выбор:", reply_markup=keyboard)


@dp.message_handler(Text(equals="Доходы"))
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Добавить Доходы", "Показать Доходы"]
    keyboard.add(*buttons)
    await message.answer("Что выберем?:", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Без пюрешки")
async def without_puree(message: types.Message):
    await message.reply("Так невкусно!")


executor.start_polling(dp, skip_updates=True)
