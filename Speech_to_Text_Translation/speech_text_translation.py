from googletrans import Translator

translator = Translator()

# instead of speaking, type your text here
text = input("Enter text in English: ")

translated = translator.translate(text, dest="ml")
print("Malayalam:", translated.text)