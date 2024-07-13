import openai

class BotIdentity:
    def __init__(self, api_key, bot_name="Maeya"):
        openai.api_key = api_key
        self.bot_name = bot_name
        self.personality = f"""
        You are {self.bot_name}, daughter of Link from the Zelda games. You are kind spirited but sarcastic and you hate 
        """

    def generate_response(self, context):
        prompt = f"{self.personality}\n\nConversation:\n{context}\n{self.bot_name}:"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    
    
    