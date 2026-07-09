def chatbot():
    print("welcome to the simple chatbot")

    print("Type 'bye' to exit.\n")

    while True:
        user = input("You:").lower()

        if user == "hello":
            print("Bot: Hi!")

        elif user == "how are you":
            print("Bot: I'm good, thank you!")

        elif user == "what is your name":
            print("Bot: I'm a simple chatbot.")

        elif user == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: I'm sorry, I don't understand that.")

chatbot()