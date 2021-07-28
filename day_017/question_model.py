from random import randint

def get_questions():
    questions = []

    while len(questions) < 4:
        random = randint(0, 11)
        if random not in questions:
            questions.append(random)
    return questions

class Question():

    def __init__(self, text,  answer):
        self.text  = text
        self.answer = answer

    def compare(self):
        print(self.text)
        if  input('True or False?: ').title() ==  self.answer:
            print('ok')
