Count = 997

while Count < 999:
    plate = input('> ')
    try:
        if int(plate[3:]) == Count + 1:
            print('Progress! [' + plate + ']')
            Count += 1
    except ValueError:
        print('ERROR, Plate isnt correct')
print('Woah 1000 counted plates!')
exit()