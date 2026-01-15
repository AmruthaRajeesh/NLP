import speech_recognition as sr
from langdetect import detect, DetectorFactory, LangDetectException
import pyttsx3

# Fix for consistent language detection
DetectorFactory.seed = 0

# Initialize recognizer and TTS engine
r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

try:
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Speak something...")
        audio = r.listen(source, timeout=5)

    # Convert speech to text
    text = r.recognize_google(audio)
    print(f"You said: {text}")

    # Check if text is not empty
    if not text.strip():
        speak("No speech detected or recognized. Please try again.")
    else:
        # Detect language safely
        try:
            language = detect(text)
        except LangDetectException:
            language = "unknown"

        # Convert language code to readable name
        language_names = {
            "en": "English",
            "fr": "French",
            "es": "Spanish",
            "de": "German",
            "it": "Italian",
            "pt": "Portuguese",
            "hi": "Hindi",
            "zh-cn": "Chinese",
            "ja": "Japanese",
            "ko": "Korean",
        }
        language_name = language_names.get(language, language)

        # Speak detected language
        speak(f"You are speaking in {language_name}")
        print(f"Detected language: {language_name}")

except sr.WaitTimeoutError:
    speak("No speech detected. Please try again.")
except sr.UnknownValueError:
    speak("Could not understand audio. Please speak clearly.")
except sr.RequestError as e:
    speak(f"API request failed. {e}")
except Exception as e:
    speak(f"Error occurred: {e}")

