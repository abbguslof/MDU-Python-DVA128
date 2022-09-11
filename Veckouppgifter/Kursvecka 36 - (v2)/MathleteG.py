print('\nWelcome to mathlete!\nEnter a finite amount of numbers and when done type exit for stats.\n')

numbersentered, sumtotal = [], 0

while True:
    Inputnumber = input('> ')
    if Inputnumber.isnumeric():
        numbersentered.append(int(Inputnumber))
    else:
        if Inputnumber.lower() == 'exit':
            for x in numbersentered:
                sumtotal = x + sumtotal
            med = sumtotal/len(numbersentered)
            print('\nAverage:',med,'\nTotal sum:',sumtotal,'\nAmount entered:',len(numbersentered),'\n')
            break
        else:
            print('ERROR: only input valid numbers or "exit".')