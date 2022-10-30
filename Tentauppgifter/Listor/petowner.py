pet_owners = [
    {'name': 'Anna', 'id': 'aa'},
    {'name': 'Lars', 'id': 'bb'},
    {'name': 'Eva', 'id': 'cc'}
]

pets = [
    {'name': 'Doris', 'owner_id': 'bb'},
    {'name': 'Molly', 'owner_id': 'cc'},
    {'name': 'Stampe', 'owner_id': 'aa'},
    {'name': 'Luna', 'owner_id': 'bb'},
    {'name': 'Pelle', 'owner_id': 'aa'}
]

pet_owner_name = input('pet owner name > ')

for dict in pet_owners:
    if dict['name'] == pet_owner_name:
        id = dict['id']
        print(f"{pet_owner_name} pets:")
        for pet in pets:
            if pet['owner_id'] == id:
                print('- ' + str(pet['name']))