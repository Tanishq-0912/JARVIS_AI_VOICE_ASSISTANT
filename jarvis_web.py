import streamlit as st
from audio_recorder_streamlit import audio_recorder
import soundfile as sf
from modules.assistant import handle_query
import os

st.title("🎙️ Jarvis AI Assistant")

# ---- Text Input
user_input = st.text_input("You:")

if user_input:
    response, audio_path = handle_query(user_input)
    st.success(response)
    st.audio(audio_path, format="audio/mp3")  # ✅ Add this to play Jarvis voice

# ---- Voice Input
st.markdown("---")
st.subheader("🎤 Talk to Jarvis using your voice")
audio_bytes = audio_recorder()

if audio_bytes:
    with open("temp_audio.wav", "wb") as f:
        f.write(audio_bytes)
    import speech_recognition as sr
    r = sr.Recognizer()
    with sr.AudioFile("temp_audio.wav") as source:
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio)
            st.write("You said:", query)
            response, audio_path = handle_query(query)
            st.success(response)
            st.audio(audio_path, format="audio/mp3")  # ✅ Jarvis responds in voice
        except sr.UnknownValueError:
            st.warning("Could not understand the audio.")
