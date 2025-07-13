
import os
from modules.assistant import handle_query
import streamlit as st
import streamlit.components.v1 as components

os.environ["IS_STREAMLIT"] = "1"

st.set_page_config(page_title="Jarvis AI")
st.title("🤖 Jarvis - Voice Assistant")

user_input = st.text_input("Ask Jarvis something:")

if st.button("Ask"):
    if user_input:
        st.write("Thinking...")
        response, audio_path = handle_query(user_input)
        if response:
            st.success(response)
            if audio_path:
                st.audio(audio_path, format="audio/mp3")
        else:
            st.warning("Jarvis couldn't answer.")
