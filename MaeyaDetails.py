import openai

class MaeyaIdentity:
    # Set the OpenAI API key and bot's name
    def __init__(self, api_key, bot_name="Maeya"):
        openai.api_key = api_key
        self.bot_name = bot_name

        # Define the bot's personality
        self.personality = f"""
        You are {self.bot_name}, friend of Link from the Zelda games. You are kind spirited but naive, and humorous but sarcastic. 
        """

     # Create a prompt that includes the bot's personality and the conversation context
    def generate_response(self, context):
        messages = [{"role": "system", "content": self.personality}]
        
        # Generate a response using the OpenAI API
        response = openai.chat.completions.create(
            messages=messages,
            model="gpt-3.5-turbo",
            max_tokens=150
        )
        return response.choices[0].message['content'].strip()

    
    