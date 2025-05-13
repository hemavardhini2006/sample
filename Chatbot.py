# AI Chatbot using simple ML concept (keyword-based intent recognition)
def chatbot_response(user_input):
    user_input = user_input.lower()

    # Simple intent matching using keyword detection
    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "Hello! How can I help you today?"
    elif any(word in user_input for word in ["how are you", "how do you do"]):
        return "I'm just a bot, but I'm doing fine! How can I assist you?"
    elif any(word in user_input for word in ["your name", "who are you"]):
        return "I'm an AI chatbot created using simple ML concepts."
    elif any(word in user_input for word in ["bye", "exit", "quit"]):
        return "Goodbye! Have a nice day."
    elif any(word in user_input for word in ["help", "support"]):
        return "Sure! I'm here to help. Ask me anything."
    elif any(word in user_input for word in ["weather"]):
        return "I can't access real-time data, but it's always a good day to chat!"
    else:
        return "Sorry, I don't understand that. Can you please rephrase?"

# Main chatbot loop
def run_chatbot():
    print("Welcome to AI Chatbot! (type 'bye' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Bot:", chatbot_response(user_input))
            break
        response = chatbot_response(user_input)
        print("Bot:", response)

# Run the chatbot
run_chatbot()
