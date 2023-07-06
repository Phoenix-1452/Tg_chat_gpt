# import openai
# import os
# from dotenv import load_dotenv
#
#
# load_dotenv()
# openai.api_key = os.getenv("API_CHAT_GPT_KEY")
# telegram_key = os.getenv("API_TG_BOT_KEY")
#
# msgs = []
#
#
# def main(message):
#     msgs.append({'role': 'user', 'content': message})
#     completion = openai.ChatCompletion.create(
#         model='gpt-3.5-turbo',
#         messages=msgs,
#         temperature=0
#     )
#     answer = completion['choices'][0]['message']['content']
#     print(answer)
#     msgs.append({'role': 'assistant', 'content': answer})
#
#
# if __name__ == '__main__':
#     while True:
#         main(input())

msgs = []
msgs.append({'role': 'assistant', 'content': 'answer'})
print(msgs)
