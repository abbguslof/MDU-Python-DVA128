print('\nWelcome to a Python Calculator! Choose, Addition(add), Subtraction(sub), Multiplication(mul) or Divide(div) and get mathing!\n')

while True:
    method = input('What method? ')
    if method.lower() == 'add':
        mathinput = input('> ')
        add = mathinput.split('+')
        sum = 0
        for x in add:
            sum = int(x) + sum
        print(mathinput,'=',sum)
    if method.lower() == 'sub':
        break
        # work in progress
    if method.lower() == 'div':
        break
        # work in progress
    if method.lower() == 'mul':
        mathinput = input('> ')
        mul = mathinput.split('*')
        sum = 1
        for x in mul:
            sum = int(x) * sum
        print(mathinput, '=', sum)
    if method.lower == 'exit':
        break
    else:
        print('please input a valid method! Add, Sub, Div, Mul.')