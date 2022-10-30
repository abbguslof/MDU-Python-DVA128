flights = [
    {'from': 'Stockholm', 'to': 'Göteborg'},
    {'from': 'Göteborg', 'to': 'Malmö'},
    {'from': 'Malmö', 'to': 'Västerås'},
    {'from': 'Göteborg', 'to': 'Stockholm'},
    {'from': 'Västerås', 'to': 'Göteborg'},
    {'from': 'Stockholm', 'to': 'Malmö'},
    {'from': 'Göteborg', 'to': 'Västerås'}
]

destinations = {}

for flight in flights:
    if flight['from'] in destinations:
       destinations[flight['from']].append(str(flight['to']))
    else:
        destinations[flight['from']] = []
        destinations[flight['from']].append(str(flight['to']))

print(str(destinations))