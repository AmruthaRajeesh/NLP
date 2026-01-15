import speech_recognition as sr
from textblob import TextBlob
import pyttsx3

# Initialize recognizer and TTS engine
r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

try:
    # Use microphone as input
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Speak something...")
        audio = r.listen(source, timeout=5)

    # Convert speech to text
    text = r.recognize_google(audio)
    print(f"You said: {text}")

    # Analyze sentiment
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    # Determine sentiment
    if polarity > 0:
        sentiment_text = "Positive"
    elif polarity < 0:
        sentiment_text = "Negative"
    else:
        sentiment_text = "Neutral"

    # Speak sentiment only
    speak(f"Your sentiment is {sentiment_text}")

except sr.WaitTimeoutError:
    speak("No speech detected. Please try again.")
except sr.UnknownValueError:
    speak("Could not understand audio. Please speak clearly.")
except sr.RequestError as e:
    speak(f"API request failed. {e}")
except Exception as e:
    speak(f"Error occurred. {e}")
