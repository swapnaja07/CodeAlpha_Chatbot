import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')  # Download NLTK data (only needed once)

pairs = [
    ["hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    ["how are you?", ["I'm good, thank you.", "I'm doing well."]],
    ["what's your name?", ["I'm a chatbot.", "You can call me Chatbot."]],
    ["website for fibonnacci series", ["https://www.geeksforgeeks.org/python-program-to-print-the-fibonacci-sequence/"]],
    ["tell me more about your self", [" Chatbots are computer programs designed to simulate conversation with human users, typically through text-based interfaces but can also include voice-based interactions."]],
    ["bye|goodbye", ["Goodbye!", "Bye! Take care."]],
]


chatbot = Chat(pairs, reflections)

print("Chatbot: Hi, I'm a chatbot. How can I help you?")
while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
    if user_input.lower() == 'bye':
        break
