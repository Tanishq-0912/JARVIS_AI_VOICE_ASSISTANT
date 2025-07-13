import streamlit as st
import tempfile
import soundfile as sf
from audio_recorder_streamlit import audio_recorder
from modules.assistant import handle_query
import speech_recognition as sr

st.set_page_config(page_title="Jarvis AI Assistant", layout="centered")
st.title("🤖 Jarvis - Your AI Voice Assistant")

# Text input option
st.markdown("### 💬 Type your message")
user_input = st.text_input("You:", "")

if user_input:
    response, audio_path = handle_query(user_input)
    st.success(response)
    if audio_path:
        st.audio(audio_path, format="audio/wav")

# Voice input option
st.markdown("---")
st.markdown("### 🎤 Talk to Jarvis using your voice")
audio_bytes = audio_recorder(pause_threshold=1.0)

if audio_bytes:
    st.audio(audio_bytes, format='audio/wav')
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        f.write(audio_bytes)
        temp_audio_path = f.name

    # Speech recognition
    recognizer = sr.Recognizer()
    with sr.AudioFile(temp_audio_path) as source:
        audio_data = recognizer.record(source)
        try:
            voice_text = recognizer.recognize_google(audio_data)
            st.markdown(f"**You said:** {voice_text}")
            response, audio_path = handle_query(voice_text)
            st.success(response)
            if audio_path:
                st.audio(audio_path, format="audio/wav")
        except sr.UnknownValueError:
            st.error("Sorry, I couldn't understand what you said.")
        except sr.RequestError:
            st.error("Speech Recognition service is unavailable. Please try again.")
