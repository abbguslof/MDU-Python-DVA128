import os
from select import select
import time
import csv

database = open('Gruppuppgifter/Case2/TodoDataBase.csv', encoding='UTF8')
csvdata = ['desc', 'checked']

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

print('\n',('#'*56),'\n')
print('████████╗ ██████╗ ██████╗  ██████╗ ██╗███████╗██╗   ██╗')
print('╚══██╔══╝██╔═══██╗██╔══██╗██╔═══██╗██║██╔════╝╚██╗ ██╔╝')
print('   ██║   ██║   ██║██║  ██║██║   ██║██║█████╗   ╚████╔╝')
print('   ██║   ██║   ██║██║  ██║██║   ██║██║██╔══╝    ╚██╔╝')
print('   ██║   ╚██████╔╝██████╔╝╚██████╔╝██║██║        ██║  ')
print('   ╚═╝    ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝        ╚═╝  ')
print('\n',('#'*56),'\n')
time.sleep(0.5)
cls()

while True:
    cls()
    print('\n', ('-'*56), '\n')
    print('list | List todos')
    print('add | Add todo')
    print('check | Check todo')
    print('delete | Delete todo')
    print('\n', ('-'*56), '\n')
    print('save | Save todos to file')
    print('load | Todos from file')
    print('\n', ('-'*56), '\n')
    select = input('Selection > ').lower()

    if select == 'list':
        cls()
        print('\n', ('-'*56), '\n')
        print('All Todos')
        print('\n', ('-'*56), '\n')
        for line in csv.reader(database):
            print(line)
        input('press enter to contiune')

    elif select == 'add':
        cls()
        print('\n', ('-'*56), '\n')
        print('Adding a todo!')
        print('\n', ('-'*56), '\n')
        add = input('Todo description > ')
        adddata = [add, '0']
        csv.writer(database).writerow(adddata)
        database.close()

    elif select == 'check':
        print('hejsan')

    elif select == 'delete':
        print('hejsan')

    elif select == 'save':
        print('hejsan')

    elif select == 'load':
        print('hejsan')

    else:
        print('hejsan')