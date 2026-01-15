import speech_recognition as sr
from textblob import TextBlob

# Initialize recognizer
r = sr.Recognizer()

try:
    # Use microphone as input
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Speak something...")
        audio = r.listen(source, timeout=5)

    # Convert speech to text
    text = r.recognize_google(audio)
    print(f"\nYou said: {text}")

    # Analyze sentiment
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    # Print sentiment
    if polarity > 0:
        print("Sentiment: Positive 😊")
    elif polarity < 0:
        print("Sentiment: Negative 😞")
    else:
        print("Sentiment: Neutral 😐")

# Error handling
except sr.WaitTimeoutError:
    print("No speech detected. Please try again.")
except sr.UnknownValueError:
    print("Could not understand audio. Please speak clearly.")
except sr.RequestError as e:
    print(f"API request failed; {e}")
except Exception as e:
    print(f"Error: {e}")
