from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import bot, dp
from keyboards import KeyboardClient
from models import User
from lang import lang
from data import UserService

@dp.message_handler(CommandStart())
async def start(message: types.Message, kb = KeyboardClient()):
    user = User(message.from_user.id, message.from_user.username, message.from_user.language_code)
    await bot.send_message(
        user.id,
        lang[user.lang]["messages"]["start"],
        reply_markup=kb.start(user.lang)
        )
    user_id = UserService.get(user.id)
    if user_id == None:
        user_id = UserService.add(user.username, user.id)
