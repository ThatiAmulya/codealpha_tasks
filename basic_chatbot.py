# Basic Chatbot - CodeAlpha Task 3

from datetime import datetime

print("================================")
print("       BASIC CHATBOT")
print("================================")
print("Hello! I am a basic chatbot.")
print("You can ask me simple questions.")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    elif "how are you" in user_input:
        print("Bot: I am fine! Thank you for asking.")

    elif "your name" in user_input:
        print("Bot: My name is CodeAlpha Chatbot.")

    elif "who are you" in user_input:
        print("Bot: I am a basic Python chatbot.")

    elif "time" in user_input:
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot: The current time is", current_time)

    elif "thank" in user_input:
        print("Bot: You're welcome!")

    elif "help" in user_input:
        print("Bot: You can say hello, ask my name, ask the time, or ask how I am.")

    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a nice day!")
        break

    else:
        print("Bot: Sorry, I don't understand that. Please try another question.")