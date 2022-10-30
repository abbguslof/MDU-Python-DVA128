birds = {'totalBirds': 0}

while True:
    birdInput = input('Bird: ')
    if birdInput.lower() not in birds:
        birds[birdInput.lower()] = 1
        birds['totalBirds'] += 1
        print(f"New bird ({birdInput}) : {birds[birdInput.lower()]} out of {birds['totalBirds']}\n")
    else:
        birds[birdInput.lower()] += 1
        birds['totalBirds'] += 1
        print(
            f"({birdInput}) : {birds[birdInput.lower()]} out of {birds['totalBirds']}\n")