correct_number = 3
guess = False
while guess == False:
    n = int(input('Try to guess my number (0-9): '))
    if n == correct_number:
        print('Yes, your guess is right!')
        guess = True
    else:
        print(f'No, it is not {n}')
print('GAME OVER')
print('THANKS FOR PLAYING')