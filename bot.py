# TODO попытка сделать домашнее задание

# 5313791416:AAGynLjrG2Jo5C0BhKiEgRPAlsjTgku-_wQ
# @try_todo_homework_bot

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery
# from key_boards import
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from tools import DBTools

bot = Bot("5313791416:AAGynLjrG2Jo5C0BhKiEgRPAlsjTgku-_wQ")
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: Message):
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    await register_user(message)
    await bot.send_message(chat_id, f"Привет {full_name}")
    await user_choice(message)


async def register_user(message: Message):
    full_name = message.from_user.full_name
    chat_id = message.chat.id
    DBTools().user_tools.register_user(full_name, chat_id)


async def user_choice(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Доходы", "Расходы"]
    keyboard.add(*buttons)
    await message.answer("Выбирайте категорию:", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Доходы")
async def user_choice_incomes(message: Message):
    await message.reply("Что украл опять?", reply_markup=ReplyKeyboardRemove())


async def user_choice_incomes_add(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Добавить доходы", "Показать доходы"]
    keyboard.add(*buttons)
    await message.answer("Выбирайте категорию:", reply_markup=keyboard)
    await user_choice(message)



@dp.message_handler(lambda message: message.text == "Расходы")
async def user_choice_expenses(message: Message):
    await message.reply("Опять просрал бабки?", reply_markup=ReplyKeyboardRemove())


executor.start_polling(dp, skip_updates=True)
