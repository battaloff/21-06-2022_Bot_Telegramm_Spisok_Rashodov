# TODO попытка сделать домашнее задание

# 5313791416:AAGynLjrG2Jo5C0BhKiEgRPAlsjTgku-_wQ
# @try_todo_homework_bot

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery
# from key_boards import
from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove,
                           CallbackQuery)
from tools import DBTools

import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.exceptions import MessageNotModified
from aiogram.utils.callback_data import CallbackData
from os import getenv
from sys import exit
from random import randint
from contextlib import suppress
import datetime

bot = Bot("5313791416:AAGynLjrG2Jo5C0BhKiEgRPAlsjTgku-_wQ")
dp = Dispatcher(bot)

user_data = {}


@dp.message_handler(commands=["start"])
async def start(message: Message):
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    await register_user(message)
    await bot.send_message(chat_id, f"Привет {full_name}")
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Доходы", "Расходы"]
    keyboard.add(*buttons)
    await message.answer("Сделайте свой выбор:", reply_markup=keyboard)


async def register_user(message: Message):
    full_name = message.from_user.full_name
    chat_id = message.chat.id
    DBTools().user_tools.register_user(full_name, chat_id)


@dp.message_handler(Text(equals="Доходы"))
async def incomes_chosen(message: Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Добавить Доходы", "Показать Доходы"]
    keyboard.add(*buttons)
    await message.answer("Что выберем?", reply_markup=keyboard)


@dp.message_handler(Text(equals="Расходы"))
async def expenses_chosen(message: Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Добавить Расходы", "Показать Расходы"]
    keyboard.add(*buttons)
    await message.answer("Что выберем?", reply_markup=keyboard)


@dp.callback_query_handler(text="Добавить Доходы")
async def send_random_value(call: CallbackQuery):
    user_id = call.message.from_user.id
    full_name = call.message.from_user.full_name
    add_income_for_user = DBTools().incomes_tools.add_income(user_id, 123, "Развлечения", str(datetime.datetime.now()))
    await add_income_for_user

    await call.message.answer()
    await call.answer(text="Спасибо, что воспользовались ботом!", show_alert=True)
    # или просто await call.answer()


executor.start_polling(dp, skip_updates=True)
