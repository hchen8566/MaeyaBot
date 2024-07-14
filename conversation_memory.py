from collections import deque

class ConversationMemory:
    # Initialize memory dictionary and set the maximum length for memory
    def __init__(self, maxlen=5):
        self.memory = {}
        self.maxlen = maxlen

    # Add a new message to the user's memory, creating a new deque if necessary
    def add_message(self, user_id, message):
        if user_id not in self.memory:
            self.memory[user_id] = deque(maxlen=self.maxlen)
        self.memory[user_id].append(message)

    # Get the conversation context for the user
    def get_context(self, user_id):
        if user_id in self.memory:
            return list(self.memory[user_id])
        return []

    # Add Maeya's response to the user's memory
    def add_bot_response(self, user_id, response):
        if user_id not in self.memory:
            self.memory[user_id] = deque(maxlen=self.maxlen)
        self.memory[user_id].append(response)