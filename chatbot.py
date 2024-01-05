from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import google.generativeai as gai
import os 

gai.configure(api_key=os.environ.get("API_KEY"))
# Load the model
model = gai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_response(prompt):
    response = chat.send_message(prompt, stream=True)
    return response

# Streamlit Code
st.set_page_config(page_title="Gemini Chatbot")
st.header("Gemini LLM Chatbot")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input:",key="input")
submit = st.button("Respond")

if submit and input:
    response = get_response(input)
    # Add user query and response to session chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot",chunk.text))
st.subheader("The chat history is")

for role,text in st.session_state['chat_history']:
    st.write(f"{role} : {text}")
