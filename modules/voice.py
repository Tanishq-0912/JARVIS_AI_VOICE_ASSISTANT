import os
import tempfile
from gtts import gTTS
import speech_recognition as sr

# For CLI mode (main.py)
def say(text):
    try:
        tts = gTTS(text)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)
            os.system(f"start {fp.name}")  # Windows
    except Exception as e:
        print(f"[Voice Error] Couldn't speak: {e}")

# For Streamlit mode (jarvis_web.py)
def generate_audio(text):
    tts = gTTS(text)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_file.name)
    return temp_file.name

# For both: voice input from mic
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = r.listen(source, timeout=5, phrase_time_limit=10)
    try:
        print("🧠 Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        return query
    except Exception as e:
        print(f"[Mic Error] {e}")
        return ""
