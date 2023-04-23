from aiogram.dispatcher.filters.state import State, StatesGroup

class ProjectStorage(StatesGroup):
    project = State()