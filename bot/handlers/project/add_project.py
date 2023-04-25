from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import bot, dp
from keyboards import KeyboardClient
from models import User
from lang import lang, lang_handl
from states import ProjectStorage
from data import ProjectService, ProjectUserService, UserService

handlers = []

for language in lang_handl:
    handlers.append(lang[language]["keyboards"]["project"][0])

@dp.message_handler(text=handlers)
async def add_project_set(message: types.Message, kb = KeyboardClient()):
    user = User(message.from_user.id, message.from_user.username, message.from_user.language_code)

    await bot.send_message(
        user.id,
        lang[user.lang]["messages"]["add_project"],
        reply_markup=kb.back(user.lang)
    )

    await ProjectStorage.project.set()

@dp.message_handler(state=ProjectStorage.project)
async def add_project(message: types.Message, state: FSMContext, kb = KeyboardClient()):
    user = User(message.from_user.id, message.from_user.username, message.from_user.language_code)
    async with state.proxy() as data:
        data["project"] = message.text  
    project_id = ProjectService.get_id(data["project"])
    user_id = UserService.get(str(user.id))
    if not project_id:
        project_id= ProjectService.add(data["project"])
    ProjectUserService.add(project_id, user_id)
    await state.finish()
    await bot.send_message(
        user.id,
        lang[user.lang]["messages"]["save"],
        reply_markup=kb.start(user.lang)
    )