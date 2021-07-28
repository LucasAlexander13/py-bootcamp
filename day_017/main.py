from question_model import *
from data import question_data

question_bank = []
question_list = get_questions()

for question in question_data:
    text = question['text']
    answer = question['answer']
    question = Question(text, answer)
    question_bank.append(question)