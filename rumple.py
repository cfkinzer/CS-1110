print('You will never win the game, for Macho Man Randy Savage is my name.')
x = input('Guess my name: ')
while x != 'Macho Man Randy Savage':
    print("Ha! You'll never guess!")
    x = input('Guess my name: ')
if x == 'Macho Man Randy Savage':
    print('No! How did you guess?')
