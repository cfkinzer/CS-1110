print("Think of a number between 1 and 100 and I'll guess it.")
x = int(input('How many guesses do I get? '))
high = 100
low = 1
guesses = 0
while guesses <= x:
    if low + 1 != high and low < high:
        half = int((low + high)/2)
        guess = input("Is the number higher, lower, or the same as {}? ".format(half))
        if guess == 'higher':
            low = half
            guesses += 1
        elif guess == 'lower':
            high = half
            guesses += 1
        elif guess == 'same':
            print("I won!")
            break
    elif low + 1 == high:
        print("Wait, how can it be higher than ", low, ' and lower than ', high, '?')
        break
if guesses == x:
    answer = int(input("I lost; what was the answer?"))
    if answer in range(low, high):
        print("Well played!")
    elif answer > high:
        print("That can't be; you said it was lower than", str(high)+'!')
    else:
        print("That can't be; you said it was lower than", str(low)+'!')
