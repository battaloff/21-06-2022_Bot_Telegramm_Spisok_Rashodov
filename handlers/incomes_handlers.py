import datetime

from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, Message

from bot import bot, dp
from database.tools import DBTools


class IncomesForm(StatesGroup):
    category = State()
    money_profit = State()
    description = State()

# TODO Дописать Finite State Machine (FSM)


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