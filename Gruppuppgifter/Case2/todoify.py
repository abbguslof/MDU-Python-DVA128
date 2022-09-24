import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
todo = ["hasse","basse","lasse"]
Completed = ["O","O","X"]
def PrintTodo():
    i = 0
    for x in todo:
        print(str(i) + " | " + "[" + Completed[i].rstrip() + "]" + todo[i])
        i += 1
def todoSelection(val):
    if val == "list":
        i = 0
        for x in todo:
            print("["+ Completed[i].rstrip("\n") + "]" + todo[i])
            i += 1
        print("-" * 40)
    elif val == "add":
        todo.append(input("Todo description > "))
        Completed.append("O")
    elif val == "check":
        PrintTodo()
        try:
            todoIndex = int(input("Todo index > "))
            if 0 <= todoIndex and todoIndex <= len(Completed):
                if Completed[todoIndex] == "O":
                    Completed[todoIndex] = "X"
                    print("-"*40 +"\nUnchecked --> Checked ")
                else:
                    Completed[todoIndex] = "O"
                    print("-"*40 + "\nChecked --> Unchecked ")
            else:
                print("ERROR: invalid index")
        except ValueError:
            print("ERROR: invalid index")
    elif val == "delete":
        PrintTodo()
        try:
            deleteTodo = int(input("Todo index > "))
            if 0 <= deleteTodo and deleteTodo <= len(todo):
                print("Deleted " + todo[deleteTodo] + " from your list")
                todo.pop(deleteTodo)
                Completed.pop(deleteTodo)
            else: 
                print("ERROR: invalid index")
        except ValueError:
            print("ERROR: invalid index")
def loadFile(filePath):
        try:
            with open(filePath, encoding="utf-8") as f:
                i = 0
                for row in f:
                    loadedTodo = row.split(",")
                    todo.append(loadedTodo[0])
                    Completed.append(loadedTodo[1])
        except FileNotFoundError:
            print("-"*20 + "\nERROR: File is not found")
def saveFile():
    with open("Todo.csv", "w") as f:
        i = 0
        for x in todo:
            f.write(todo[i] + "," + Completed[i] + "\n")
            i += 1
while True:
    cls()
    print("*" * 40)
    print("Todoify".center(40, " "))
    print("-" * 40)
    print("list   | List todos")
    print("add    | Add todo")
    print("check  | Check todo")
    print("delete | Delete todo")
    print("-" * 40)
    print("save   | Save todos to file")
    print("load   | Load todos from file")
    print("-" * 40)
    select = input("Selection > ").lower()
    if select == "list" or select == "add" or select == "check" or select == "delete":
        todoSelection(select)
        input("press enter to continue")
    elif select == "save":
        saveFile()
        print("-"*40 + "\n" +"Succesfully saved your file as Todo.csv\n")
        input("press enter to continue...")
    elif select == "load":
        fPath = input("file name > ")
        loadFile(fPath)
        input("Press enter to continue...")
    else:
        print("ERROR: Unknown command")
        input("Press enter to continue...")
