from question_model import *
from data import question_data

question_bank = []
question_list = get_questions()
score = 0

for question in question_data:
    text = question['text']
    answer = question['answer']
    question = Question(text, answer)
    question_bank.append(question)

for i  in range(1, 5):
    index =  question_list[i - 1]

    print(f'Q.{i}: {question_bank[index].text}')

    if question_bank[index].compare():
        score += 1
        print(f'You current score is {score}/{i}\n')
    else:
        print(f'You current score is {score}/{i}\n')
