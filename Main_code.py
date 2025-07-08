# Rule-Based ChatBot - Source Code

def get_bot_response(user_input, user_name):
    # Predefined responses stored as key-value pairs
    responses = {
        "your name": f"My name is ViratBot, {user_name}!",
        "how are you": "I’m doing great, ready to answer your questions.",
        "what is python": "Python is a high-level, easy-to-learn programming language.",
        "who made you": "I was built by a CSE student named Mani.",
        "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
        "what's up": "Just running some clean code and chatting with you!"
    }

    # Match user input with known responses
    for key in responses:
        if key in user_input:
            return responses[key]

    # Default response if no match found
    return "I didn’t understand that. Try asking something else."

def chatbot():
    print("Hello! I am ViratBot - your rule-based chatbot.")
    user_name = input("Before we begin, what's your name? ")

    print(f"Nice to meet you, {user_name}! You can start asking me questions.")
    print("Type 'bye', 'exit', or 'quit' to end the chat.\n")

    while True:
        user_input = input(f"{user_name}: ").lower()

        # Exit condition
        if user_input in ['bye', 'exit', 'quit']:
            print(f"ViratBot: Goodbye {user_name}, take care!")
            break

        # Get response from the bot
        response = get_bot_response(user_input, user_name)
        print(f"ViratBot: {response}")

# Run the chatbot
chatbot()
