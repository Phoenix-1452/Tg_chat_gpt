from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv
import os
import openai

load_dotenv()
TELEGRAM_KEY = os.getenv("API_TG_BOT_KEY")
openai.api_key = os.getenv("API_CHAT_GPT_KEY")

bot = Bot(TELEGRAM_KEY)
dp = Dispatcher(bot)

msg = {}


@dp.message_handler(commands=['start'])
async def start_msg(message: types.Message):
    await message.answer("Hello, this is CHAT GPT telegram bot.")


@dp.message_handler(commands=['history'])
async def gpt_history(message: types.Message):
    await message.answer(str(msg))


@dp.message_handler(commands=['clear'])
async def gpt_history(message: types.Message):
    msg.clear()
    await message.answer("History deleted.")


@dp.message_handler()
async def gpt_answer(message: types.Message):
    flood = await message.answer('Generating...')
    if not (message.from_user.id in msg):
        msg[message.from_user.id] = []
    msg[message.from_user.id].append({'role': 'user', 'content': message.text})

    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=msg[message.from_user.id],
        temperature=0.5
    )

    answer = completion['choices'][0]['message']['content']
    await message.reply(answer)
    await flood.delete()
    msg[message.from_user.id].append({'role': 'assistant', 'content': answer})


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
