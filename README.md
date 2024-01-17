# Gemini Chatbot

**Engage in interactive conversations with Google AI's Gemini LLM through a user-friendly Streamlit app!**


Gemini Chatbot is a conversational AI application built using the Google GenerativeAI (genai) library and Streamlit. It allows users to interact with a language model, Gemini Pro, to have natural language conversations.


## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Prerequisites](#prerequisites)
- [Usage](#usage)

## Features

- **Contextual Chat**: Maintains an ongoing conversation with the model, building context over multiple exchanges.
- **Chunked Response**: Displays responses as they are generated, providing a more engaging experience.
- **Chat History**: Keeps track of the conversation, allowing you to revisit previous exchanges.
- **Error Handling**: Gracefully handles potential errors during model loading or communication.

## Installation

1. Clone this repository:
  ```bash
  git clone https://github.com/deepak-porwal04/gemini-qabot.git
  ```

2. Install the required dependencies:
  ```
  pip install -r requirements.txt
  ```
3. Set up the environment variables:

 - Create a `.env` file in the project root directory.

- Add your Gemini API key to the `.env` file:
```bash
API_KEY=your_gemini_api_key
  ```
4. Run the Streamlit application:
  ```
  streamlit run app.py
  ```

## Prerequisites

- `python>=3.9`: Designed using python 3.9 
- `streamlit`: Streamlit library for building web applications.
- `google.generativeai`: Gemini API for generative models.
- `python-dotenv`: To store the environment variables secretly

## Usage

1. Input your query in the provided text input.
2. Click the "Respond" button to receive a response from the Gemini Pro model.
3. The app will display the model's response, updating it as it's generated.
4. Continue the conversation by entering more queries.
5. Review the chat history to see the full conversation flow.


