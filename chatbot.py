def chatbot():
    print("Chatbot: Hello! I am a simple rule-based bot. Type 'bye' to exit.")

    while True:
        # 1. Get user input and convert to lowercase
        user_input = input("You: ").lower()

        # 2. Rule-based Logic
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello there! How can I help you today?")
        
        elif "how are you" in user_input:
            print("Chatbot: I'm doing great, thank you for asking! How about you?")
        
        elif "your name" in user_input:
            print("Chatbot: I am your friendly Python Chatbot created for my internship.")

        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break  # Stops the loop
        
        else:
            print("Chatbot: I'm sorry, I don't understand that. Could you try saying 'hello'?")

# Run the chatbot
chatbot()