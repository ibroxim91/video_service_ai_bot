import os
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from aiogram.types import Update
from bot import bot, dp
from dotenv import load_dotenv

load_dotenv()

WEBHOOK_URL = os.getenv("WEBHOOK_URL")

@asynccontextmanager
async def lifespan(app: FastAPI):
    await bot.set_webhook(WEBHOOK_URL)
    yield
    await bot.delete_webhook()

app = FastAPI(lifespan=lifespan)

@app.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    update = Update.model_validate(data)   
    await dp.feed_update(bot, update)      
    return {"ok": True}



@app.get("/")
def hello_index():
    return {
        "message": "Hello index!",
    }
