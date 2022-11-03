from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
import asyncio, handlers
from config import token, owmtoken, admin_id
from pyowm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
loop = asyncio.get_event_loop()
bot = Bot(token, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)


if __name__ == "__main__":
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)
