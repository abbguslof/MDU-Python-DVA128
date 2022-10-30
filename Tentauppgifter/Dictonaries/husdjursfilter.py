def pet_filter(listOfDictWithPets):
    catDogs = []
    for dict in listOfDictWithPets:
        if dict['type'] in ['cat', 'dog']:
            catDogs.append(dict)
    return catDogs

pets = [
    {'name': 'Smulan', 'type': 'cat'},
    {'name': 'Molly', 'type': 'dog'},
    {'name': 'Stampe', 'type': 'rabbit'},
    {'name': 'Bella', 'type': 'cat'},
    {'name': 'Blubbe', 'type': 'fish'},
    {'name': 'Morris', 'type': 'dog'}
]

cat_and_dogs = pet_filter(pets)

for pet in cat_and_dogs:
    print(pet["name"], '(' + pet["type"] + ')')