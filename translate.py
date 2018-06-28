from googletrans import Translator

translator = Translator()

trans = translator.translate('i have a gun', dest='ko')
print(trans.text)