countries = {
    "Sweden": ["Stockholm", "Göteborg", "Malmö"],
    "Norway": ["Oslo", "Bergen", "Trondheim"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": ["Paris", "Marseille", "Toulouse"]
}
cityToLower = []
city = input('city > ')

for country in countries:
    cityToLower = []
    for x in range(len(countries[country])):
        cityToLower.append(countries[country][x].lower())
    if city.lower() in cityToLower:
        print(country)
        exit()
else:
    print(f"Error: did not find ({city})")