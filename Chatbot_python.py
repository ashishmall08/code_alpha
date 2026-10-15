def chatbot():
    print("🤖 Chatbot: Hello! I am your chatbot.")
    print("Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "hello" or user == "hi":
            print("🤖 Chatbot: Hello! How are you?")

        elif user == "how are you":
            print("🤖 Chatbot: I'm fine, thanks! How are you?")

        elif user == "what is your name":
            print("🤖 Chatbot: My name is Python Bot.")

        elif user == "bye":
            print("🤖 Chatbot: Goodbye! Have a nice day!")
            break

        else:
            print("🤖 Chatbot: Sorry, I don't understand that.")

chatbot()