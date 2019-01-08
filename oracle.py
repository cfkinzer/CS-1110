import random

def answer():
    a = random.randrange(7)
    if a == 0:
        return 'Yes'
    if a == 1:
        return 'No'
    if a == 2:
        return 'Definitely'
    if a == 3:
        return 'You wish'
    if a == 3:
        return 'Wait and see'
    if a == 4:
        return "You won't like the answer"
    if a == 5:
        return "Unsure. Ask again"
    if a == 6:
        return 'Maybe'

def oracle():
    question = input('What would you like to ask the oracle?')
    if question.startswith('Who'):

