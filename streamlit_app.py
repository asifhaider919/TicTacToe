import streamlit as st
import nltk
from nltk.tokenize import word_tokenize

# Download NLTK resources (run once)
nltk.download('punkt')

# Function to process user input and generate response
def process_message(message):
    tokens = word_tokenize(message.lower())
    
    # Define keywords and corresponding responses
    responses = {
        ("hi", "hello", "hey"): "Hello! How can I assist you?",
        ("how", "are", "you"): "I'm good, thank you! How about you?",
        ("bye", "goodbye"): "Goodbye! Have a great day!"
    }

    # Check for keywords in user input
    for key_words, response in responses.items():
        if any(word in tokens for word in key_words):
            return response

    # Default response for unrecognized input
    return "I'm sorry, I don't understand. Could you please rephrase?"

# Main function to run the Streamlit app
def main():
    st.title("Dynamic Chatbot")

    # Input box for user to enter messages
    user_input = st.text_input("Enter a message:")
    if user_input:
        # Display user input
        st.text(f"You: {user_input}")

        # Process user input and get chatbot response
        bot_response = process_message(user_input)
        st.text(f"ChatBot: {bot_response}")

if __name__ == "__main__":
    main()
