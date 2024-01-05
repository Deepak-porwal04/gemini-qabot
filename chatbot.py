import streamlit as st
import google.generativeai as gai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()  # Load variables from .env file

# Configure GenerativeAI API key
gai.configure(api_key=os.environ.get("API_KEY"))  # Set API key from environment

# Load Gemini Pro model and start chat
model = gai.GenerativeModel("gemini-pro")  # Load the Gemini Pro model
chat = model.start_chat(history=[])  # Initiate a chat session

def get_response(prompt):
   """
   Sends a prompt to the model and returns the response in chunks.

   Args:
       prompt (str): The prompt to send to the model.

   Returns:
       Iterator[str]: An iterator over the response chunks.
   """

   response = chat.send_message(prompt, stream=True)  # Send prompt and receive response
   return response  # Return response chunks

# Create Streamlit app
st.set_page_config(page_title="Gemini Chatbot")  # Set page title
st.header("Gemini LLM Chatbot")  # Display header

# Initialize chat history in session state
if 'chat_history' not in st.session_state:
   st.session_state['chat_history'] = []  # Create empty chat history list

# Input section
input = st.text_input("Input:", key="input")  # Text input for user query
submit = st.button("Respond")  # Button to submit query

if submit and input:
   response = get_response(input)  # Get response from model

   # Add user query and response to chat history
   st.session_state['chat_history'].append(("You", input))  # Add user input to history
   st.subheader("The response is")  # Display subheader for response

   for chunk in response:
       if chunk.text:  # Only display non-empty chunks
           st.write(chunk.text)  # Display response chunk
           st.session_state['chat_history'].append(("Bot", chunk.text))  # Add bot response to history

st.subheader("The chat history is")  # Display subheader for chat history

for role, text in st.session_state['chat_history']:
   st.write(f"{role}: {text}")  # Display chat history with roles
