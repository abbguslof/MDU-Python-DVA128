import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

while True:
    print("_________________________\n")
    print("Mathlete Calculator")
    print("_________________________")
    print("add | Add two numbers")
    print("sub | Subtract two numbers")
    print("mul | Multiply two numbers")
    print("div | divide two numbers")
    print("__________________________")
    op = input("Selection >  ")
    if op.lower() == "add":
        print("_______________________")
        print("calculating 'c' for expression:\n")
        print("     a + b = c\n")
        print("please enter value for 'a' and 'b'.\n")
        a = input("a = ")
        b = input("b = ")
        print()
        try:
            c = float(a) + float(b)
            print()
            if c == int(c):
                c = int(c)
            print("Result: " + str(a) + " + " + str(b) + " = " + str(c) + "\n") 
            input("Press enter to continue...")
            cls()
        except ValueError:
            print("ERROR: invalid expression ' " + str(a) + " + " + str(b) + " '\n")
            input("press enter to continue...")
            cls()

    elif op.lower() == "sub":
        print("_______________________")
        print("calculating 'c' for expression:\n")
        print("     a - b = c\n")
        print("please enter value for 'a' and 'b'.\n")
        a = input("a = ")
        b = input("b = ")
        print()
        try:
            c = float(a) - float(b)
            print()
            if c == int(c):
                c = int(c)
            print("Result: " + str(a) + " - " + str(b) + " = " + str(c) + "\n")
            input("Press enter to continue...")
            cls()
        except ValueError:
            print("ERROR: invalid expression ' " + str(a) + " - " + str(b) + " '\n")
            input("press enter to continue...")
            cls()
    elif op.lower() == "mul":
        print("_______________________")
        print("calculating 'c' for expression:\n")
        print("     a * b = c\n")
        print("please enter value for 'a' and 'b'.\n")
        a = input("a = ")
        b = input("b = ")
        print()
        try:
            c = float(a) * float(b)
            print()
            if c == int(c):
                c = int(c)
            print("Result: " + str(a) + " * " + str(b) + " = " + str(c) + "\n")
            input("Press enter to continue...")
            cls()
        except ValueError:
            print("ERROR: invalid expression ' " + str(a) + " * " + str(b) + " '\n")
            input("press enter to continue...")
            cls()
    elif op.lower() == "div":
        print("_______________________")
        print("calculating 'c' for expression:\n")
        print("     a / b = c\n")
        print("please enter value for 'a' and 'b'.\n")
        a = input("a = ")
        b = input("b = ")
        print()
        try:
            c = float(a) / float(b)
            if c == int(c):
                c = int(c)
            print()
            print("Result: " + str(a) + " / " + str(b) + " = " + str(c) +"\n")
            input("Press enter to continue...")
            cls()
        except ValueError:
            print("ERROR: invalid expression ' " +
                  str(a) + " / " + str(b) + " '\n")
            input("press enter to continue...")
            cls()
    elif op == "":
        cls()   
    else:
        print("ERROR: unknown command " + "'" + op + "'" )
        input("Press enter to continue...")
        cls()

