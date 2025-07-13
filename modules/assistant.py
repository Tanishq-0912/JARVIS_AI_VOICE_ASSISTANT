import os
import webbrowser
from modules.chatbot import query_together
from config import together_api_key
from modules.voice import takeCommand
from modules.voice import generate_audio

# Conditional voice support
if os.environ.get("IS_STREAMLIT"):
    from modules.voice import generate_audio
else:
    from modules.voice import say

def handle_query(query):
    query = query.lower()
    response = query_together(query)
    audio_path = generate_audio(response)
    return response, audio_path

    # ---- Handle Web Commands ----
    if "open google" in query:
        if not os.environ.get("IS_STREAMLIT"):
            say("Opening Google")
        webbrowser.open("https://www.google.com")
        return "Opened Google", None

    elif "open youtube" in query:
        if not os.environ.get("IS_STREAMLIT"):
            say("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
        return "Opened YouTube", None

    elif "open instagram" in query:
        if not os.environ.get("IS_STREAMLIT"):
            say("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
        return "Opened Instagram", None

    elif "open chatgpt" in query or "open chat gpt" in query:
        if not os.environ.get("IS_STREAMLIT"):
            say("Opening ChatGPT")
        webbrowser.open("https://chat.openai.com")
        return "Opened ChatGPT", None

    # ---- Chatbot Mode ----
    response = query_together(query)

    if os.environ.get("IS_STREAMLIT"):
        audio_path = generate_audio(response)
        return response, audio_path
    else:
        say("Thinking...")
        say(response)
        return response, None
