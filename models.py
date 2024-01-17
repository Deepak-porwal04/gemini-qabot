import google.generativeai as gai
import logging
def load_model(api_key: str) -> gai.GenerativeModel:
    """Loads the Gemini Pro model."""
    gai.configure(api_key=api_key)
    logging.info("Model configured")
    return gai.GenerativeModel("gemini-pro")

def start_chat(model: gai.GenerativeModel) -> gai.chat:
    """Starts a chat session with the model."""
    logging.info("Chat session started")
    return model.start_chat(history=[])
