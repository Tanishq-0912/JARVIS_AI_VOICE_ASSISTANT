import os
import streamlit as st
from modules.assistant import handle_query
from modules.voice import takeCommand

os.environ["IS_STREAMLIT"] = "1"

st.set_page_config(page_title="Jarvis AI")
st.title("🤖 Jarvis - Your AI Assistant")

st.markdown("Ask something by typing or using your voice 🎤")

# Text input
user_input = st.text_input("Type your question:")

# Voice input
use_mic = st.button("🎤 Speak Instead")

# Processing input
if st.button("Ask") or use_mic:
    if use_mic:
        st.info("Listening for your voice input...")
        try:
            user_input = takeCommand()
            st.success(f"Recognized: {user_input}")
        except Exception as e:
            st.error(f"Mic error: {e}")
            user_input = ""

    if user_input:
        st.write("Thinking...")
        response, audio_path = handle_query(user_input)
        st.success(response)

        # Play audio
        if audio_path:
            st.audio(audio_path, format="audio/mp3")
    else:
        st.warning("Please type or speak something.")
