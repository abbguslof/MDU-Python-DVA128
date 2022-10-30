def print_all_keys(dictonary):
    for key, value in dictonary.items():
        if type(value) is dict:
            print(key)
            print_all_keys(value)
        else:
            print(key)

person = {
    'namn': 'Petra Svensson',
    'bostad': {
        'typ': 'hyra',
        'avgift': 5000
    },
    'husdjur': {
        'Douglas': {
            'typ': 'hund'
        },
        'Stampe': {
            'typ': 'kanin'
        }
    }
}

print_all_keys(person)