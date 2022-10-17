InputedNumbers, tot = [], 0

while True:
    InputNumber = input('> ')
    try:
        if InputNumber == 'exit':
            for i in range(len(InputedNumbers)):
                tot += InputedNumbers[i]
            print('mean: ' + str(tot/len(InputedNumbers)))
            break
        elif int(InputNumber):
            InputedNumbers.append(int(InputNumber))
    except:
        print('value error')