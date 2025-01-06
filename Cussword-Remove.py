from better_profanity import profanity #swear word

input_text=input("Enter your text: ")
censored_text=profanity.censor(input_text)
print(censored_text)