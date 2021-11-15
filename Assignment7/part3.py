import random

correct = random.randint(1, 9)

while int(input('Guess a number from 1 to 9')) != correct:
    x = 'oof'

print('Well Guessed!')
