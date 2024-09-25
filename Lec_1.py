from translate import Translator

inserted_text = "Python is so Powerful"
translator = Translator(to_lang="hi")
translation = translator.translate(inserted_text)

print(translation)
