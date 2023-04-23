from models import Keyboard

class KeyboardClient(Keyboard):

    def start(self, user_lang):
        return self._keyboard(user_lang, "start")
    
    def channel(self, user_lang):
        return self._keyboard(user_lang, "channel")
    
    def project(self, user_lang):
        return self._keyboard(user_lang, "project")

    def back(self, user_lang):
        return self._keyboard(user_lang, "back")