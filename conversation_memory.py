from collections import deque

class ConversationMemory:
    def __init__(self, maxlen=5):
        self.memory = {}
        self.maxlen = maxlen

    def add_message(self, user_id, message):
        if user_id not in self.memory:
            self.memory[user_id] = deque(maxlen=self.maxlen)
        self.memory[user_id].append(message)

    def get_context(self, user_id):
        if user_id in self.memory:
            return "\n".join(self.memory[user_id])
        return ""

    def add_bot_response(self, user_id, response):
        if user_id not in self.memory:
            self.memory[user_id] = deque(maxlen=self.maxlen)
        self.memory[user_id].append(response)