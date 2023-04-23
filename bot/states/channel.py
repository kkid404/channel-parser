from aiogram.dispatcher.filters.state import State, StatesGroup

class ChannelStorage(StatesGroup):
    channel = State()