from collections import deque

class ConversationMemory:
    # Initialize memory dictionary and set the maximum length for memory
    def __init__(self, maxlen=3):
        self.memory = deque(maxlen=maxlen)

    # Add a new message to the user's memory, creating a new deque if necessary
    def add_message(self, message):
        self.memory.append(message)

    # Get the conversation context for the user
    def get_context(self):
        return list(self.memory)

    # Add Maeya's response to the user's memory
    def add_bot_response(self, response):
        self.memory.append(response)