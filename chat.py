import nltk
from nltk.chat.util import Chat, reflections

# Download NLTK data (if not already downloaded)
nltk.download('punkt')

# Define a simple set of rules for the chatbot
chatbot_pairs = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'How can I help you?']),
    (r'how are you', ["I'm doing well, thank you!", "I'm fine, how about you?"]),
    (r'quit|exit|bye', ['Goodbye!', 'See you later!', 'Have a great day!']),
    (r'my name is (.*)', ["Nice to meet you, {}!", "Hello, {}!"]),
    (r'what is your name', ["I am a simple chatbot.", "You can call me ChatBot."]),
    (r'(.*)', ['I am not sure how to respond.']),
]

# Create a chat instance
chatbot = Chat(chatbot_pairs, reflections)

# Define a function to interact with the chatbot
def chat_with_bot():
    print("Hello! I'm creating a chatbot for assignment . You can start chatting with me. Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ").lower()

        if user_input == 'exit':
            print("Chatbot: Goodbye! Have a great day.")
            break

        response = chatbot.respond(user_input)
        print("Chatbot:", response)