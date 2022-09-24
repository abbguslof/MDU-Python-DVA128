import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
todo = ["hasse","basse","lasse"]
Completed = [" "," ","x"]
def PrintTodo():
    i = 0
    for x in todo:
        print(str(i) + " | " + "[" + Completed[i] + "]" + todo[i])
        i += 1
def todoChange(val):
    if val == "list":
        i = 0
        for x in todo:
            print("["+ Completed[i] + "]" + todo[i])
            i += 1
        print("-" * 40)
    elif val == "add":
        todo.append(input("Todo description > "))
        Completed.append(" ")
    elif val == "check":
        PrintTodo()
        try:
            todoIndex = int(input("Todo index > "))
            if 0 < todoIndex and todoIndex < len(Completed):
                if Completed[todoIndex] == " ":
                    Completed[todoIndex] = "x"
                else:
                    Completed[todoIndex] = " "
            else:
                print("ERROR: invalid index")
        except ValueError:
            print("ERROR: invalid index")
    elif val == "delete":
        PrintTodo()
        try:
            deleteTodo = int(input("Todo index > "))
            if 0 < todoIndex and todoIndex < len(todo):
                todo.pop(deleteTodo)
                Completed.pop(deleteTodo)
            else: 
                print("ERROR: invalid index")
        except ValueError:
            print("ERROR: invalid index")
def fileUser(val):
    if val == "save":
        with open("Todo.csv", "x") as f:
            i = 0
            for x in todo:
                f.write("'" + todo[i] + "'")

    elif val == "load":
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
    todoChange("check")
    select = input("Selection > ").lower().strip()
