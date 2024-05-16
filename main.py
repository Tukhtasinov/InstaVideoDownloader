import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from func import video_download

load_dotenv()
TOKEN = getenv("BOT_TOKEN")
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Salom, {html.bold(message.from_user.full_name)}!")


@dp.message(lambda msg: msg.text.startswith('https://www.instagram.com/reel/'))
async def echo_handler(message: Message) -> None:
    try:
        video_url = message.text
        text = f"""{video_url}  
        
Ushbu Botdan foydalangangiz uchun raxmat 😊   


@doniyorbeks_bot"""
        video = video_download(video_url)
        await message.answer_video(video, caption=text)
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
