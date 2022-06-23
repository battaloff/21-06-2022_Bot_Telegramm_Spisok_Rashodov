from aiogram.types.inline_keyboard import (
    InlineKeyboardMarkup, InlineKeyboardButton
)
from aiogram.types.reply_keyboard import (
    ReplyKeyboardMarkup, KeyboardButton
)
from tools import DBTools


def generate_choice_city_menu(message: Message):
    markup = InlineKeyboardMarkup(
        InlineKeyboardButton("Доходы", callback_data="incomes"),
        InlineKeyboardButton("Расходы", callback_data="but_2")
    )  # Клавиатура / Разметка

    return markup

# def generate_save_city_menu(city_name: str):
#     markup = InlineKeyboardMarkup()  # Клавиатура / Разметка
#     markup.row(
#         InlineKeyboardButton(text="Сохранить город", callback_data=f"save_{city_name}")
#     )
#     return markup
#
# def generate_choice_menu(user_id: str):
#     markup1 = InlineKeyboardMarkup()  # Клавиатура / Разметка
#     markup1.row(
#         InlineKeyboardButton(text="Доходы")
#     )
#     markup2 = InlineKeyboardMarkup()  # Клавиатура / Разметка
#     markup2.row(
#         InlineKeyboardButton(text="Расходы")
#     )
#     return markup1, markup2
#
#
# def inline_key_board(incomes, expenses):
#     keyboard = InlineKeyboardMarkup(row_width=2)
#     button_update = InlineKeyboardButton(text="Доходы", callback_data=f"save_{incomes}")
#     button_bwt = InlineKeyboardButton(text="Расходы", callback_data=f"save_{expenses}")
#     keyboard.add(button_update, button_bwt)
#     return keyboard
