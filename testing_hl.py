import random
global answer
answer = int(input('What should the answer be? '))
n = int(input('How many guesses? '))
if answer == -1:
    answer = random.randint(1, 100)
global guess
guess = int(input('Guess a number: '))
for i in range(n - 1):
    if guess > answer:
        print('The number is lower than that.')
        guess = int(input('Guess a number: '))
    if guess < answer:
        print('The number is higher than that.')
        guess = int(input('Guess a number: '))
    if guess == answer:
        print('You win!')
if guess != answer:
    print('You lose; the number was ', answer)
