import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

todo, Completed, breakline = [], [], '\n'+'-'* 40

def PrintTodo():
    i = 0
    for x in todo:
        print(str(i) + ' | ' + '[' + Completed[i] + '] ' + todo[i])
        i += 1

def todoSelection(val):
    if val == 'list':
        i = 0
        for x in todo:
            print('['+ Completed[i].rstrip('\n') + '] ' + todo[i])
            i += 1
    elif val == 'add':
        todo.append(input('Todo description > '))
        Completed.append('O')
    elif val == 'check':
        PrintTodo()
        try:
            todoIndex = int(input('Todo index > '))
            if 0 <= todoIndex and todoIndex <= len(Completed):
                if Completed[todoIndex] == 'O':
                    Completed[todoIndex] = 'X'
                    print(breakline.strip('\n') + '\nUnchecked --> Checked ')
                else:
                    Completed[todoIndex] = 'O'
                    print(breakline.strip('\n') + '\nChecked --> Unchecked ')
            else:
                print('ERROR: Todo not existent')
        except ValueError:
            print('ERROR: invalid index')
    elif val == 'delete':
        PrintTodo()
        try:
            deleteTodo = int(input('Todo index > '))
            if 0 <= deleteTodo and deleteTodo <= len(todo):
                print('Deleted ' + todo[deleteTodo] + ' from your list')
                todo.pop(deleteTodo)
                Completed.pop(deleteTodo)
            else: 
                print('ERROR: Todo not existant')
        except ValueError:
            print('ERROR: invalid index')

def loadFile(filePath):
    try:
        with open(filePath, encoding='utf-8') as f:
            for row in f:
                loadedTodo = row.split(',')
                todo.append(loadedTodo[0])
                Completed.append(loadedTodo[1].rstrip('\n'))
    except FileNotFoundError:
        print(breakline.strip('\n') + '\nERROR: File is not found')

def saveFile():
    with open('Gruppuppgifter/Case2/Todo.csv', 'w', encoding='utf-8') as f:
        i = 0
        for x in todo:
            f.write(todo[i] + ',' + Completed[i] + '\n')
            i += 1

while True:
    cls()
    print('*' * 40)
    print('Todoify'.center(40, ' '), breakline)
    print('list   | List todos')
    print('add    | Add todo')
    print('check  | Check todo')
    print('delete | Delete todo', breakline)
    print('save   | Save todos to file')
    print('load   | Load todos from file', breakline)
    select = input('Selection > ').lower()
    if select == 'list' or select == 'add' or select == 'check' or select == 'delete':
        todoSelection(select)
    elif select == 'save':
        saveFile()
        print(breakline.strip('\n') + '\nSuccesfully saved your file as Todo.csv')
    elif select == 'load':
        loadFile(input('Relative Filepath > '))
    else:
        print('ERROR: Unknown command')
    print(breakline.strip('\n'))
    input('Press enter to continue...')