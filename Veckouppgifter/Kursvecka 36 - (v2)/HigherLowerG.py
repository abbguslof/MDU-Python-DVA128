import random
print('\nHello and welcome to a game of Higher Lower!\nA random number between 1 and 100 will be generated and you will try guess it! Good luck.')

randnum, guesses = random.randint(1, 100), 1
guess = input('Whats your guess? ')

while guess.isnumeric():
    if randnum != int(guess):
            if int(guess) < randnum:
                print("Higher!")
            else:
                print("Lower!")
            guesses = guesses + 1
            guess = input("Try again: ")
    else:
            print('Woah you guessed right! in', guesses, 'guesses.')
            exit()
else:
        print('ERROR! Please only use numbers.')