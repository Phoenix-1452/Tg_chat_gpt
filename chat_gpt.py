import openai


class ChatGpt:
    def __init__(self, history, message):
        self.completion = {}
        self.history = history
        self.message = message

    def run(self):
        self.completion = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=self.history[self.message.from_user.id],
            temperature=1.0
        )

    def get_answer(self):
        return self.completion['choices'][0]['message']['content']



