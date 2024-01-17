import streamlit as st
import logging
import google.generativeai as gai
def get_response(chat: gai.chat, prompt: str) -> str:
    """
    Sends a prompt to the provided GenerativeAI Chat object and returns the text response in chunks.

    Args:
        chat (gai.Chat): The active chat session object from Google GenerativeAI.
        prompt (str): The text prompt to send to the model for generation.

    Returns:
        Iterator[str]: An iterator that yields response text chunks one at a time.

    Raises:
        RuntimeError: If the chat object is not valid or an error occurs during communication.
    """

    logging.info(f"Sending prompt: {prompt}")
    response = chat.send_message(prompt, stream=True)  # Send prompt for chunked response
    return response

def handle_user_query(chat: gai.chat, input: str, session_state: st.session_state) -> None:
    """
    Processes user input, generates a response using the provided chat object, and updates the chat history.

    Args:
        chat (gai.Chat): The active chat session object from Google GenerativeAI.
        input (str): The user's text query input.
        session_state (st.SessionState): The Streamlit session state object to store chat history.

    Raises:
        ValueError: If the user input is empty.
    """

    logging.info(f"Received user input: {input}")

    if not input:
        raise ValueError("Please enter your query to get a response.")

    response = get_response(chat, input)  # Get response for user input

    session_state['chat_history'].append(("You", input))

    # Display response with progress bar and update chat history
    with st.spinner("Generating response..."):
        for chunk in response:
            if chunk.text:
                st.write(chunk.text)
                st.session_state['chat_history'].append(("Bot", chunk.text))

    