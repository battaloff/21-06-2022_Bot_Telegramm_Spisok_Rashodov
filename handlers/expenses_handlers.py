import datetime

from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, Message

from bot import bot, dp
from database.tools import DBTools


class ExpensesForm(StatesGroup):
    category = State()
    money_expended = State()
    description = State()


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
async def get_expenses_by_year(message: Message):
    chat_id = message.chat.id
    user_id = DBTools().user_tools.get_user_id(chat_id)
    expenses = DBTools().expenses_tools.get_expenses_by_year(user_id)
    await bot.send_message(chat_id, f"Ваши расходы за этот год: {expenses} сум")
