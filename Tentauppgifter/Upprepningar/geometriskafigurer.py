shape = input('shape: ')
height = int(input('height: '))
loop = 1

if shape.lower() == 'rectangle':
    width = int(input('width: '))
    while loop <= height:
        print('#'*width)
        loop += 1
elif shape.lower() == 'triangle':
    while height >= loop:
        print('#'*loop)
        loop += 1