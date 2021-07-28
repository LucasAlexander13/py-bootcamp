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
        if  input('True or False?: ').title() ==  self.answer:
            print('\nYou got it right!')
            print(f'The correct answer was: {self.answer}')
            return True
        else:
            print('\nThat\'s wrong.')
            print(f'The correct answer was: {self.answer}')
            return False
