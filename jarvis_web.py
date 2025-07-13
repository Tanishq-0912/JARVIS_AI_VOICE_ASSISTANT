import streamlit as st
from audio_recorder_streamlit import audio_recorder
import soundfile as sf
from modules.assistant import handle_query
import os
import speech_recognition as sr

st.set_page_config(page_title="Jarvis AI Assistant", page_icon="🎙️")

st.title("🎙️ Jarvis AI Assistant")

# ---- Text Input
user_input = st.text_input("Type your message here:")

if user_input:
    with st.spinner("🤖 Jarvis is thinking..."):
        response, audio_path = handle_query(user_input)
    st.success(response)
    st.audio(audio_path, format="audio/mp3")  # ✅ Play Jarvis's voice

# ---- Voice Input Section
st.markdown("---")
st.subheader("🎤 Talk to Jarvis using your voice")

st.write("Click the mic below to start recording ⬇️")
audio_bytes = audio_recorder(pause_threshold=3.0)

if audio_bytes:
    st.info("✅ Voice recorded. Processing...")
    
    # Save audio to a temporary file
    with open("temp_audio.wav", "wb") as f:
        f.write(audio_bytes)

    # Use SpeechRecognition to transcribe
    r = sr.Recognizer()
    with sr.AudioFile("temp_audio.wav") as source:
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio)
            st.markdown(f"🗣️ You said: **{query}**")

            # Handle the query
            with st.spinner("🤖 Jarvis is thinking..."):
                response, audio_path = handle_query(query)
            st.success(response)
            st.audio(audio_path, format="audio/mp3")

        except sr.UnknownValueError:
            st.warning("😕 Sorry, I couldn't understand your voice.")
