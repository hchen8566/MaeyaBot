from googletrans import Translator

class Language:
    def __init__(self):
        self.translator = Translator()

    def detect_language(self, text):
        detection = self.translator.detect(text)
        return detection.lang

    def translate_text(self, text, target_language):
        translation = self.translator.translate(text, dest=target_language)
        return translation.text