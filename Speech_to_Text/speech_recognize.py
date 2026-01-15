import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Please speak...")
    try:
        audio = r.listen(source, timeout=5)
        print(r.recognize_google(audio))
    except sr.WaitTimeoutError:
        print("You did not speak. Please speak.")
    except sr.UnknownValueError:
        print("I heard something, but could not understand. Please speak clearly.")
