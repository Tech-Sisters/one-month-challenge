import streamlit as st
from dataclasses import dataclass
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Set up the header with an emoji and description to introduce the chatbot
st.markdown("# 👭 Tech Sisters Assistant")
st.markdown("This is a friendly assistant, here to provide information about Tech Sisters. Whether looking to learn more about the community, events, or values, assistance is available. Let's start connecting!")

# Define the data structure for chat messages using a dataclass
@dataclass
class ChatMessage:
    """Represents a single chat message."""
    sender: str  # The actor who sent the message (user or assistant)
    content: str # The content of the message

# Constants for message actors
USER = "user"
ASSISTANT = "ai"
gemini_api_key = os.getenv('GOOGLE_GEMINI_API')

# Configure the Google Generative AI with the API key
genai.configure(api_key=gemini_api_key)

# Initialize the session state for storing messages
if "messages" not in st.session_state:
    # Set up initial conversation history with a default assistant message
    st.session_state.messages = []

def format_chat(messages):
    """Format chat messages for API call."""
    chat_history = []
    for message in messages:
        chat_history.append({
            "role": "user" if message.sender == USER else "model",
            "parts": [message.content]
        })
    return chat_history

def ai_response(history):
    """
    Generate a response from the assistant based on the chat history.
    
    Args:
        history (list): The list of chat messages.
    
    Returns:
        str: The assistant's generated response.
    """
    # Read the prompt template from a file
    prompt_path = os.path.join(os.path.dirname(__file__), "prompt.txt")
    prompt = open(prompt_path, "r").read() 

    # Initialize the AI model with the specified model name and the formatted chat history
    model = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction=prompt)

    # Start the chat with the existing history
    chat = model.start_chat(history=format_chat(history))
    
    # Get the latest user input to send to the AI model
    latest_user_message = history[-1].content if history else ""

    # Generate the AI response based on the chat history
    response = chat.send_message(content=latest_user_message).text
    
    return response

# Display the chat messages
for message in st.session_state.messages:
    st.chat_message(message.sender).write(message.content)

# Input box for user to type a message
user_input: str = st.chat_input("Ask me anything...")

# If the user has entered a prompt, process the input
if user_input:
    # Add the user's message to the chat history
    st.session_state.messages.append(ChatMessage(sender=USER, content=user_input))
    st.chat_message(USER).write(user_input)

    # Display a spinner while the AI is generating a response
    with st.spinner("Generating response..."):
        # Generate a response from the assistant
        assistant_response: str = ai_response(st.session_state.messages)

    # Add the assistant's response to the chat history
    st.session_state.messages.append(ChatMessage(sender=ASSISTANT, content=assistant_response))
    st.chat_message(ASSISTANT).write(assistant_response)
