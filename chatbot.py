# chatbot.py

print("Welcome to CodSoft ChatBot!")
print("Type 'exit' to end the chat.\n")

while True:
    user_input = input("You: ").lower()

    if user_input in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you today?")

    elif "your name" in user_input:
        print("Bot: I'm CodSoft ChatBot, your virtual assistant.")

    elif "help" in user_input:
        print("Bot: I can help you with general questions. Try asking about my name or greet me!")

    elif "weather" in user_input:
        print("Bot: Sorry, I can't check the weather right now, but you can try Google!")

    elif "bye" in user_input or "exit" in user_input:
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: I'm not sure how to respond to that. Try something else.")