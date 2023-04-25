from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from typing import Union
from lang import lang

class Keyboard:
    def _keyboard(self, user_lang: str, name: str, row_width: int = 2) -> Union[ReplyKeyboardMarkup, InlineKeyboardMarkup]:
        """
        Creates a keyboard from a list of strings or a dictionary.
        Args:
            btns (Union[list, dict]): A list of strings or a dictionary of the form {code: button name}.
            row_width (int): The number of buttons in a row.
        Returns:
            Union[ReplyKeyboardMarkup, InlineKeyboardMarkup]: The keyboard created.
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