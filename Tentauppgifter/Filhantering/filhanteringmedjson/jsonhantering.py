import json
readfile = open('Tentauppgifter/Filhantering/filhanteringmedjson/numbers.json',)
data = json.load(readfile)
readfile.close()

newint = data[0] * 2
data.insert(0, newint)

writefile = open('Tentauppgifter/Filhantering/filhanteringmedjson/numbers.json', 'w')

# Onödigt men schysst för att lätt kunna gå tillbaka till orginal fil
input = input('Revert? y/n ').lower()
if input == 'y':
    writefile.write(str([8, 4, 2, 1]))
else:
    # Det viktiga
    writefile.write(str(data))

writefile.close()