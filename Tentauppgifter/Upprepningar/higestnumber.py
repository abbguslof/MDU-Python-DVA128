inputedNumbers, higest = [], 0

while True:
    currentnumber = input('> ')
    try:
        if int(currentnumber) == 0:
            for x in range(len(inputedNumbers)):
                if inputedNumbers[x] > higest:
                    higest = inputedNumbers[x]
            print(higest)
            break
        elif int(currentnumber):
            inputedNumbers.append(int(currentnumber))
    except ValueError:
        print('ValueError')