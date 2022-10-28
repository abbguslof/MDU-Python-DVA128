Numbers, Total = [], 0

while True:
    CurrentNumber = input('> ')
    try:
        if int(CurrentNumber) == 0:
            for i in range(len(Numbers)):
                Total += Numbers[i]
            print('sum = ' + str(Total))
            break
        elif int(CurrentNumber):
            Numbers.append(int(CurrentNumber))
    except ValueError:
        print('value error')