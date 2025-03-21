# Importing libraries and dependencies
import discord
import config
from config import discordToken, apiKey, spotify_id, spotify_secret
from conversation_memory import ConversationMemory
from MaeyaDetails import MaeyaIdentity
from music import Music
from language import Language

# Set up intents for the bot to receive message content
intents = discord.Intents.default()
intents.message_content = True

# Initialize the Discord client with the specified intent
client = discord.Client(intents=intents)

# Initialize conversation memory and bot identity
conversation_memory = ConversationMemory()
bot_identity = MaeyaIdentity(apiKey, bot_name="Maeya")

# Loading music cog commands from music.py and pass in Spotify credentials
music = Music(client, spotify_id, spotify_secret)

# Initialize language support
language = Language()

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
    
    # Check if the message is a command and handle music commands
    if message.content.startswith('!'):
        command, *args = message.content[1:].split()
        if command == "join":
            await music.join(message)
        elif command == "leave":
            await music.leave(message)
        elif command == "play":
            query = ' '.join(args)
            await music.play(message, query)
        elif command == "stop":
            await music.stop(message)
        return
    
    # Detecting language of request
    detected_language = language.detect_language(message.content)
    print(f"Detected language: {detected_language}")

    # Translate message to English if it's not already in English
    if detected_language != 'en':
        translated_content = language.translate_text(message.content, 'en')
        message_content = f"{message.author.name}: {translated_content} (translated from {detected_language})"
    else:
        message_content = f"{message.author.name}: {message.content}"
    
    # Add the new message to the user's conversation memory
    conversation_memory.add_message({"role": "user", "content": f"{message.author.name}: {message.content}"})

    if "maeya" not in message.content.lower():
        # Ignore messages that do not mention Maeya's name
        return
    
    # Retrieve the conversation context for the user
    context = conversation_memory.get_context()
    #print(context) #DUBUG!!!
    
    # Generate a response based on the context and bot's personality
    answer = bot_identity.generate_response(context)
    

    # Translate the response back to the detected language if necessary
    if detected_language != 'en':
        answer = language.translate_text(answer, detected_language)
        response_content = f"Maeya: {answer} (translated to {detected_language})"
    else:
        response_content = f"Maeya: {answer}"

    # Add the bot's response to the user's conversation memory
    conversation_memory.add_bot_response({"role": "assistant", "content": answer})

    # Send the response back to the channel
    await message.channel.send(answer)

# Run the bot with the specified token
client.run(discordToken)