import os
from dotenv import load_dotenv

load_dotenv()

# Getting tokens and api keys from enviroment variables
discordToken = os.getenv('discordToken')
apiKey = os.getenv('openAIKey')

# Check if the environment variables are loaded correctly
if not discordToken:
    raise ValueError("Discord Token is not set in the environment variables.")
if not apiKey:
    raise ValueError("API Key is not set in the environment variables.")