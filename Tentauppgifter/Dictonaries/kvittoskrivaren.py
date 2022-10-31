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
totalPrice = 39
print('Kvitto'.center(48))
print('-'*48)

for thing in cart:
	print(f"{thing['quantity']} st {thing['name']} ({thing['cost']}kr/st)")
	totalPrice += thing['quantity'] * thing['cost']

print('-'*48)
print('fraktavgift: 39 kr')
print('totalkostnad: ' + str(totalPrice) + ' kr')