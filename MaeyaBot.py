#import and libraries
import os
import discord
import openai
from dotenv import load_dotenv
from collections import deque

load_dotenv()

# Getting tokens and api keys from enviroment variables
discordToken = os.getenv('discordToken')
apiKey = os.getenv('openAIKey')

# Check if the environment variables are loaded correctly
if not discordToken:
    raise ValueError("Discord Token is not set in the environment variables.")
if not apiKey:
    raise ValueError("API Key is not set in the environment variables.")

# Setting up Discord Intents for Bot (tells bot what data to take in)
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Assinging api key to openAI
openai.api_key = apiKey

# Dictionary to store conversation context with a deque for limited memory
conversation_memory = {}

# Event handlers for when Bot is ready and active
@client.event
async def on_ready():
    print(f'Bot is ready as {client.user}')

# Event handlers for messages
@client.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return

    # Assign messages author to a user variable (used for storing conversations later)
    user_id = message.author.id

    # Initialize memory for new user with a deque to limit memory size
    if user_id not in conversation_memory:
        conversation_memory[user_id] = deque(maxlen=5)

    # Add the new message to the user's memory
    conversation_memory[user_id].append(f"{message.author.name}: {message.content}")

    # Create a context by joining the messages in memory
    context = "\n".join(conversation_memory[user_id])

    # Generate a response based on the context
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"The following is a conversation with a helpful assistant. Respond appropriately.\n{context}",
        max_tokens=150
    )
    answer = response.choices[0].text.strip()

    # Add the bot's response to the user's memory
    conversation_memory[user_id].append(f"{client.user.name}: {answer}")

    await message.channel.send(answer)

client.run(discordToken)
