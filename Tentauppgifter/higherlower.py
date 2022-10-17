import random
print('higher lower 0-99')
rndint = random.randint(0,99)
guessint = int(input('> '))

while True:
    if guessint != rndint:
        if guessint < rndint:
            print('Higher')
        else:
            print('Lower')
        guessint = int(input('> '))
    else:
        break

print('You Won!')