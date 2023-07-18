import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
import os
import openai

from chat_gpt import ChatGpt
from models.create_data import registration, buy_vip, prompts, get_history, clear_history

load_dotenv()
TELEGRAM_KEY = os.getenv("API_TG_BOT_KEY")
openai.api_key = os.getenv("API_CHAT_GPT_KEY")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TELEGRAM_KEY, parse_mode="HTML")
dp = Dispatcher()


@dp.message(Command("start"))
async def start_msg(message: types.Message):
    await message.answer("Hello, this is CHAT GPT telegram bot.")
    user_id = message.from_user.id
    registration(user_id)


@dp.message(Command("clear"))
async def gpt_history(message: types.Message):
    # history.clear()
    user_id = message.from_user.id
    clear_history(user_id)
    await message.answer("History deleted.")


@dp.message()
async def gpt_answer(message: types.Message):
    flood = await message.answer('Generating...')

    user_id = message.from_user.id

    prompts(user_id, {'role': 'user', 'content': message.text})

    chat = ChatGpt(get_history(user_id), message)
    chat.run()
    answer = chat.get_answer()

    await message.reply(answer)
    await flood.delete()
    prompts(user_id, {'role': 'assistant', 'content': answer})


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
