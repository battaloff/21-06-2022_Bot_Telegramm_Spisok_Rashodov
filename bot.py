# TODO попытка сделать домашнее задание

# 5313791416:AAGynLjrG2Jo5C0BhKiEgRPAlsjTgku-_wQ
# @try_todo_homework_bot


from aiogram import Bot, Dispatcher, executor
from dotenv import load_dotenv
import os

load_dotenv()

bot = Bot(os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)

if __name__ == "__main__":
    from handlers import *
    executor.start_polling(dp, skip_updates=True)
