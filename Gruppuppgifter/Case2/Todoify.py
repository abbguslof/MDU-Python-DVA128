import os
import time

data = open('Gruppuppgifter/Case2/TodoDataBase.csv', 'w')
# csv.writer(data).writerow()
data.close()

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
time.sleep(1)
cls()

def menu():
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
    return input('Selection > ')

while True:
    menu()
    break