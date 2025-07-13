
import requests
from config import together_api_key
import streamlit as st
together_api_key   = "097a44384fe5a42bc7d469f0d86eb61c489526d7fdc805c9ab976de568424067"

def query_together(prompt):
    url = "https://api.together.xyz/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {together_api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistralai/Mistral-7B-Instruct-v0.1",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 200
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Together API error: {e}")
        return "I'm sorry, I couldn't process that."
