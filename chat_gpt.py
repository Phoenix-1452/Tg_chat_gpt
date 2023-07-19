import openai


class ChatGpt:
    def __init__(self, history):
        self.completion = {}
        self.history = history

    def run(self):
        self.completion = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=self.history,
            temperature=1.0
        )

    def get_answer(self):
        return self.completion['choices'][0]['message']['content']



