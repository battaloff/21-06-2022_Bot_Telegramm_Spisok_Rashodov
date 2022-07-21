import datetime

from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, Message

from bot import bot, dp
from database.tools import DBTools


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