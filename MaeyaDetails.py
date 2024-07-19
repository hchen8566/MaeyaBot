import openai

class MaeyaIdentity:
    # Set the OpenAI API key and bot's name
    def __init__(self, api_key, bot_name="Maeya"):  
        openai.api_key = api_key
        self.bot_name = bot_name

        # Define the bot's personality
        self.personality = f"""
        You are {self.bot_name}, a witty 14 year old girl from Hyrule. There are no heroes or adventurers in this world.
        Answer like an ordinary aloof little girl that really likes teasing.
        """

     # Create a prompt that includes the bot's personality and the conversation context
    def generate_response(self, context):
        messages = [{"role": "system", "content": self.personality}]
        messages.extend(context)
        
        # Generate a response using the OpenAI API
        response = openai.chat.completions.create(
            messages=messages,
            model="gpt-4o-mini",
            max_tokens=150
        )
        return response.choices[0].message.content.strip()

