import logging
import streamlit as st
from config import load_config
from models import load_model, start_chat
from utils import handle_user_query

# Logging setup
logging.basicConfig(level=logging.INFO)

# Load API key and initialize model and chat
api_key = load_config("API_KEY")

try:
    model = load_model(api_key)
    chat = start_chat(model)
except Exception as e:
    st.error(f"Error loading model or starting chat: {e}")
    st.stop()

# Streamlit app configuration and header
st.set_page_config(page_title="Gemini Chatbot")
st.header("Gemini LLM Chatbot")

# Input section for user query
input = st.text_input("Input:", key="input")
submit = st.button("Respond")

if submit and input:
    try:
        if 'chat_history' not in st.session_state:
            st.session_state['chat_history'] = []  # Create empty chat history list
        handle_user_query(chat, input, st.session_state)
    except ValueError as e:
        st.error(e)

# Display chat history with role labels
st.subheader("Chat History:")
for role, text in st.session_state.get('chat_history', []):
    st.write(f"{role}: {text}")