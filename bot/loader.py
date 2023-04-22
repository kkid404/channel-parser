import os
import configparser
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
HOST = os.getenv("DB_HOST")
USERNAME = os.getenv("DB_USERNAME")
PASSWORD = os.getenv("DB_PASSWORD")
DATABASE = os.getenv("DB_DATABASE")
PORT = os.getenv("DB_PORT")
storage = MemoryStorage()
bot = Bot(TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)