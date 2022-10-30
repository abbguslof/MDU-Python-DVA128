countries = {
    'Denmark': ['red', 'white'],
    'Finland': ['white', 'blue'],
    'France': ['blue', 'white', 'red'],
    'Germany': ['black', 'red', 'yellow'],
    'Iceland': ['blue', 'white', 'red'],
    'Netherlands': ['red', 'white', 'blue'],
    'Norway': ['red', 'white', 'blue'],
    'Sweden': ['yellow', 'blue'],
    'Ukraine': ['blue', 'yellow']
}

colors = input('colors > ').split()

for country in countries:
    if all(x in countries[country] for x in colors):
        print(country)