import pyttsx3

# initialize engine
engine = pyttsx3.init()

# input text
text = input("Enter text in English: ")

# speak text
engine.say(text)
engine.runAndWait()