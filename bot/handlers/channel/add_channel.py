from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import bot, dp
from keyboards import KeyboardClient
from models import User
from lang import lang, lang_handl
from states import ChannelStorage
from data import ChannelService

handlers = []

for language in lang_handl:
    handlers.append(lang[language]["keyboards"]["channel"][0])

@dp.message_handler(text=handlers)
async def add_channel_set(message: types.Message, kb = KeyboardClient()):
    user = User(message.from_user.id, message.from_user.username, message.from_user.language_code)

    await bot.send_message(
        user.id,
        lang[user.lang]["messages"]["add_channel"],
        reply_markup=kb.back(user.lang)
    )

    await ChannelStorage.channel.set()

@dp.message_handler(state=ChannelStorage.channel)
async def add_channel(message: types.Message, state: FSMContext, kb = KeyboardClient()):
    user = User(message.from_user.id, message.from_user.username, message.from_user.language_code)
    async with state.proxy() as data:
        data["channel"] = message.text  
    if ChannelService.get_link(data["channel"]) == False:
        ChannelService.add(data["channel"])
    await state.finish()
    await bot.send_message(
        user.id,
        lang[user.lang]["messages"]["save"],
        reply_markup=kb.start(user.lang)
    )