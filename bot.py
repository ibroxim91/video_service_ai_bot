import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv
from app.open_ai import get_sql_from_question
from db.queries import execute_query

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

@dp.message()
async def handle_text(message: Message):
    sql_query = get_sql_from_question(message.text)
    if sql_query == "None":
        await message.answer("Неверный запрос")
        return
    result = execute_query(sql_query)
    await message.answer(str(result))