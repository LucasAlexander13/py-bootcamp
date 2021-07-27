from question_model import *
from data import question_data

question_bank = []

for question in question_data:
    text = question['text']
    answer = question['answer']
    question = Question(text, answer)
    question_bank.append(question)

print(question_bank)

