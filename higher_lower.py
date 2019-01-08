import random
answer = int(input('What should the answer be? '))
n = int(input('How many guesses? '))
if answer == -1:
    answer = random.randint(1, 100)
global x
x = 1
while x < n:
    global guess
    guess = int(input('Guess a number: '))
    x += 1
    if guess < answer:
        print('The number is higher than that.')
    if guess > answer:
        print('The number is lower than that.')
    if guess == answer:
        print('You win!')
        break
while x == n:
    guess = int(input('Guess a number: '))
    if guess != answer:
        print('You lose, the number was ', answer)
    if guess == answer:
        print('You win!')
    break
