from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from typing import Union
from lang import lang

class Keyboard:
    def _keyboard(self, user_lang: str, name: str, row_width: int = 2) -> Union[ReplyKeyboardMarkup, InlineKeyboardMarkup]:
        """
        Создает клавиатуру из списка строк или словаря.
        Args:
            btns (Union[list, dict]): Список строк или словарь вида {код: название кнопки}.
            row_width (int): Количество кнопок в строке.
        Returns:
            Union[ReplyKeyboardMarkup, InlineKeyboardMarkup]: Созданная клавиатура.
        """
        btns = lang[user_lang]["keyboards"][name]
        if isinstance(btns, list):
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=row_width)
            keyboard.add(*btns)
        elif isinstance(btns, dict):
            keyboard = InlineKeyboardMarkup(row_width=row_width)
            for code, name in btns.items():
                btn = InlineKeyboardButton(name, callback_data=code)
                keyboard.add(btn)
        return keyboard