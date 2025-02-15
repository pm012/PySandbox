from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import spacy

nlp = spacy.load("en_core_web_sm")
# Create a chatbot instance

bot = ChatBot("My Bot")

# Create a trainer for the bot
trainer = ChatterBotCorpusTrainer(bot)

# Train the bot on same conversation data
trainer.train("chatterbot.corpus.english.greetings", "chatterbot.corpus.english.conversations")

#Start a conversation with the bot
while True:
    user_input = input("User (ort type 'exit' to quit): ")
    if user_input == "exit":
        break
    response = bot.get_response(user_input)
    print("Bot: ", response)