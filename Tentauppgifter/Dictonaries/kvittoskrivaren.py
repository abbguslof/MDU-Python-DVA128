cart = [
    {
        'name': 'T-shirt',
        'quantity': 2,
        'cost': 149
    },
    {
        'name': 'Shorts',
        'quantity': 1,
        'cost': 199
    },
    {
        'name': 'Strumpor',
        'quantity': 3,
        'cost': 49
    },
    {
        'name': 'Baddräkt',
        'quantity': 1,
        'cost': 249
    }
]
countedCart = {}
totPrice = 0

for items in cart:
    if items['name'] in countedCart:
        countedCart[items['name']][0] += int(items['quantity'])
    else:
        countedCart[items['name']] = [int(items['quantity']), int(items['cost'])]

print('Kvitto'.center(22))
print('-'*22)

for x in countedCart:
    print(f"{countedCart[x][0]} st {x} ({countedCart[x][1]}/st)")
    totPrice += (countedCart[x][0] * countedCart[x][1])

print('-'*22)
print('Fraktavgift: 39 kr')
print('Total kostnad: ' + str(totPrice + 39) + ' kr')