from models import Keyboard

class KeyboardClient(Keyboard):

    def start(self, user_lang):
        return self._keyboard(user_lang, "start")