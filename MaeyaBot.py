# Importing libraries and dependencies
import discord
from config import discordToken, apiKey
from conversation_memory import ConversationMemory
from MaeyaDetails import MaeyaIdentity

# Set up intents for the bot to receive message content
intents = discord.Intents.default()
intents.message_content = True

# Initialize the Discord client with the specified intents
client = discord.Client(intents=intents)

# Initialize conversation memory and bot identity
conversation_memory = ConversationMemory()
bot_identity = MaeyaIdentity(apiKey, bot_name="Maeya")

@client.event
async def on_ready():
    # Event handler for when the bot is ready
    print(f'Bot is ready as {client.user}')

@client.event
async def on_message(message):
    # Event handler for when a message is received
    if message.author == client.user:
        # Ignore messages sent by the bot itself
        return

    user_id = message.author.id
    
    # Add the new message to the user's conversation memory
    conversation_memory.add_message(user_id, {"role": "user", "content": message.content})
    
    # Retrieve the conversation context for the user
    context = conversation_memory.get_context(user_id)
    
    # Generate a response based on the context and bot's personality
    answer = bot_identity.generate_response(context)
    
    # Add the bot's response to the user's conversation memory
    conversation_memory.add_bot_response(user_id, {"role": "assistant", "content": answer})

    # Send the response back to the channel
    await message.channel.send(answer)

# Run the bot with the specified token
client.run(discordToken)
