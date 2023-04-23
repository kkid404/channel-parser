from aiogram import types

from loader import bot, dp
from keyboards import KeyboardClient
from models import User
from lang import lang, lang_handl

handlers = []

for language in lang_handl:
    handlers.append(lang[language]["keyboards"]["start"][0])

@dp.message_handler(text=handlers)
async def channel(message: types.Message, kb = KeyboardClient()):
    user = User(message.from_user.id, message.from_user.username, message.from_user.language_code)
    await bot.send_message(
        user.id,
        lang[user.lang]["messages"]["do"],
        reply_markup=kb.channel(user.lang)
    )