car_colors = [
    'red',
    'green',
    'black',
    'blue',
    'white',
    'blue',
    'black/red',
    'red',
    'blue',
    'black',
    'white',
    'black/red'
]

carscount, splitcolors = {}, []

for color in car_colors:
    splitcolors.append(color)
    carscount[color] = 0

for count in splitcolors:
    carscount[count] += 1

for countedcar in carscount:
    print(countedcar + ', ' + str(carscount[countedcar]))