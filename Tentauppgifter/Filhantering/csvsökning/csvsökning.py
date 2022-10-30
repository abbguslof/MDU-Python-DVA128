db = []
with open('Tentauppgifter\Filhantering\csvsökning\db.csv', encoding='utf-8') as file:
    for row in file:
        LoadedFile = row.split(',') 
        db.append(LoadedFile)

location = input('Loaction: ')
print('-'* len(location))
for x in range(len(db)):
    if location == db[x][2].strip('\n'):
        print(f"{db[x][0]}, {db[x][1]}, " + str(db[x][2].strip('\n')))