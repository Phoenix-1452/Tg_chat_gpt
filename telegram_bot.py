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
bot = Bot(token=TELEGRAM_KEY)
dp = Dispatcher()

kb = [
    [types.KeyboardButton(text="/clear")],
    [types.KeyboardButton(text="/buy_vip")],
    [types.KeyboardButton(text="/info")]

]
keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)


@dp.message(Command(commands=["start", "info"]))
async def start_msg(message: types.Message):
    await message.answer(text="<b>Hello, this is CHAT GPT telegram bot.</b>\n"
                              "<b>list of bot commands:</b>\n"
                              "<em>/clear - clear context</em>\n"
                              "<em>/buy_vip - buy vip status for gpt 4</em>\n"
                              "<em>/info - information about bot</em>",
                         reply_markup=keyboard,
                         parse_mode="HTML")
    user_id = message.from_user.id
    registration(user_id)


@dp.message(Command("buy_vip"))
async def start_msg(message: types.Message):
    user_id = message.from_user.id
    buy_vip(user_id)
    await message.answer("OK")


@dp.message(Command("clear"))
async def gpt_history(message: types.Message):
    user_id = message.from_user.id
    clear_history(user_id)
    await message.answer("History deleted.")


@dp.message()
async def gpt_answer(message: types.Message):
    flood = await message.answer('Generating...')
    user_id = message.from_user.id

    try:
        prompts(user_id, {'role': 'user', 'content': message.text})
        chat = ChatGpt(get_history(user_id))
        chat.run()
        answer = chat.get_answer()
        await message.reply(answer)
        await flood.delete()
        prompts(user_id, {'role': 'assistant', 'content': answer})
    except Exception:
        await flood.delete()
        await message.answer('Token Limit Exceeded!!!'
                             'We have deleted the history of your requests, ask your question again')
        clear_history(user_id)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
