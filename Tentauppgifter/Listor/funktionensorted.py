people = [
    {
        'name': 'Anna',
        'age': 25
    },
    {
        'name': 'Lars',
        'age': 20
    },
    {
        'name': 'Eva',
        'age': 30
    }
]

people.sort(key=lambda x: x.get('age'), reverse=True)
sortedpeople = sorted(people, key=lambda x: x.get('age'), reverse=True)

for person in people:
    print(f"{person['name']} - {person['age']}")

print('\n people.Sort(): Above, Sorted(): Below\n')

for person in sortedpeople:
    print(f"{person['name']} - {person['age']}")