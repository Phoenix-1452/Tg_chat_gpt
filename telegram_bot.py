import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
import os
import openai
from chat_gpt import ChatGpt

load_dotenv()
TELEGRAM_KEY = os.getenv("API_TG_BOT_KEY")
openai.api_key = os.getenv("API_CHAT_GPT_KEY")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TELEGRAM_KEY, parse_mode="HTML")
dp = Dispatcher()

history = {}


@dp.message(Command("start"))
async def start_msg(message: types.Message):
    await message.answer("Hello, this is CHAT GPT telegram bot.")


@dp.message(Command("history"))
async def gpt_history(message: types.Message):
    await message.answer(str(history))


@dp.message(Command("clear"))
async def gpt_history(message: types.Message):
    history.clear()
    await message.answer("History deleted.")


@dp.message()
async def gpt_answer(message: types.Message):
    flood = await message.answer('Generating...')
    if not (message.from_user.id in history):
        history[message.from_user.id] = []
    history[message.from_user.id].append({'role': 'user', 'content': message.text})

    # completion = openai.ChatCompletion.create(
    #     model='gpt-3.5-turbo',
    #     messages=history[message.from_user.id],
    #     temperature=1.0
    # )

    chat = ChatGpt(history, message)
    chat.run()
    answer = chat.get_answer()

    # answer = completion['choices'][0]['message']['content']
    await message.reply(answer)
    await flood.delete()
    history[message.from_user.id].append({'role': 'assistant', 'content': answer})


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
