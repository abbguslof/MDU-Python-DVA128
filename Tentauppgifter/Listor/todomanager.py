todos = []

while True:
    print('\n\n_- Todo Manager -_')
    print('List | list todos')
    print('Add | add a todo')
    print('rm | remove a todo')
    UserSelection = input('> ').lower()

    if UserSelection == 'list':
        for todo in todos:
            print('| ' + todo)
        input('press enter to continue')
    elif UserSelection == 'add':
        AddTodo = str(input('> '))
        if AddTodo not in todos:
            todos.append(AddTodo)
            print(str(AddTodo) + ' was added')
        input('press enter to continue')
    elif UserSelection == 'rm':
        RmTodo = input('> ')
        if RmTodo in todos:
            todos.remove(str(RmTodo))
            print(str(RmTodo) + ' was removed')
        input('press enter to continue')
    else:
        print('sorry dont recognize that command')
        input('press enter to continue')