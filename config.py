import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Getting tokens and api keys from enviroment variable
# Passing them onto variables to be used for the Discord Bot and API
discordToken = os.getenv('discordToken')
apiKey = os.getenv('openAIKey')
spotify_id = os.getenv('spotify_client_id')
spotify_secret = os.getenv('spotify_secret')

# Check if the environment variables are loaded correctly
if not discordToken:
    raise ValueError("Discord Token is not set in the environment variables.")
if not apiKey:
    raise ValueError("API Key is not set in the environment variables.")
if not spotify_id:
    raise ValueError("Spotify client id is not set in the environment variables.")
if not spotify_secret:
    raise ValueError("Spotify secret key is not set in the environment variables.")