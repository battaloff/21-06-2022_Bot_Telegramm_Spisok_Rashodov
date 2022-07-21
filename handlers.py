import datetime

from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, Message

from bot import bot, dp
from tools import DBTools


@dp.message_handler(commands=["start"])
async def start(message: Message):
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    await register_user(message)
    await bot.send_message(chat_id, f"Привет {full_name}")
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["🔽  Доходы", "🔼  Расходы"]
    keyboard.add(*buttons)
    await message.answer("Сделайте свой выбор:", reply_markup=keyboard)


async def register_user(message: Message):
    full_name = message.from_user.full_name
    chat_id = message.chat.id
    DBTools().user_tools.register_user(full_name, chat_id)


@dp.message_handler(Text(equals="🔽  Доходы"))
async def incomes_chosen(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["➕  Добавить Доходы", "🙈  Показать Доходы"]
    keyboard.add(*buttons)
    await message.answer("Что выберем?", reply_markup=keyboard)


@dp.message_handler(Text(equals="➕  Добавить Доходы"))  # TODO пишу сюда добавление доходов
async def show_incomes_by_user(message: Message):
    chat_id = message.chat.id
    user_id = DBTools().user_tools.get_user_id(chat_id)
    date_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    income = DBTools().incomes_tools.add_income(user_id, int(input()), date_time)
    await bot.send_message(chat_id, f"Ваши доходы, {income} !")


@dp.message_handler(Text(equals="🙈  Показать Доходы"))
async def show_incomes_by_user(message: Message):
    chat_id = message.chat.id
    user_id = DBTools().user_tools.get_user_id(chat_id)
    incomes = DBTools().incomes_tools.get_incomes_by_user(user_id)
    await bot.send_message(chat_id, f"Ваши доходы: {incomes} сум")


@dp.message_handler(Text(equals="🔼  Расходы"))
async def expenses_chosen(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["➕  Добавить Расходы", "Показать Расходы"]
    keyboard.add(*buttons)
    await message.answer("Что выберем?", reply_markup=keyboard)


@dp.message_handler(Text(equals="Показать Расходы"))
async def expenses_chosen(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    buttons = ["За Год", "За Месяц", "За неделю", "За День"]
    keyboard.add(*buttons)
    await message.answer("Что выберем?", reply_markup=keyboard)


@dp.message_handler(Text(equals="За Год"))
async def show_incomes_by_user(message: Message):
    chat_id = message.chat.id
    user_id = DBTools().user_tools.get_user_id(chat_id)
    incomes = DBTools().expenses_tools.get_expenses_by_datetime_and_user(user_id)
    await bot.send_message(chat_id, f"Ваши доходы: {incomes} сум")