import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import os

TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
menu_kb.add(KeyboardButton("Мануалы"), KeyboardButton("Аккаунты"))

manuals = [
    {"title": "Мануал: Как заработать 100$", "link": "https://example.com/manual1"},
    {"title": "Мануал: Автоматизация в Telegram", "link": "https://example.com/manual2"}
]

accounts = [
    {"title": "Telegram аккаунт RU", "link": "https://example.com/account1"},
    {"title": "Telegram аккаунт USA", "link": "https://example.com/account2"}
]

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Добро пожаловать в магазин! Выберите категорию:", reply_markup=menu_kb)

@dp.message_handler(lambda message: message.text == "Мануалы")
async def show_manuals(message: types.Message):
    text = "\n\n".join([f"{m['title']}\n➡ {m['link']}" for m in manuals])
    await message.answer(f"Доступные мануалы:\n\n{text}")

@dp.message_handler(lambda message: message.text == "Аккаунты")
async def show_accounts(message: types.Message):
    text = "\n\n".join([f"{a['title']}\n➡ {a['link']}" for a in accounts])
    await message.answer(f"Доступные аккаунты:\n\n{text}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)