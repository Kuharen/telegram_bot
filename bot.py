import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import Message

TOKEN = "7558207788:AAFNOz0CqHV-j49-Qbs6wtByGiciBa9aPwc"

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message()
async def handle_message(message: Message):
    await message.answer("Привет! Бот работает 24/7 на Render.com 🟢")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
