import os, requests, json
def cls(val):
    os.system('cls' if os.name=='nt' else 'clear')
    if val:
        print(BreakLine('-') + '\n' + 'Artist Database'.center(40) + '\n' + BreakLine('-'))

def BreakLine(character):
    return str(character)*40

def getArtists(id,key):
    a = requests.get('https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/' + str(id))
    artists = json.loads(a.text)[key]
    return artists

def errorMessage(reason, instance):
    print(BreakLine('-') + '\n| ERROR: ' + instance + ' ' + str(reason) + ' \n' + BreakLine('-'))
    input('Press enter to continue')
    cls(True)

def printMenu():
    print('| L | List artists')
    print('| V | View artist profile')
    print('| E | Exit program\n' + BreakLine('-'))
cls(True)
while True:
    printMenu()
    op = input('| Selection > ').lower().strip()
    if op in ['l', 'v', 'e']:
        cls(True)
    if op == 'l':
        artists = getArtists('', 'artists')
        for artist in artists:
            print(artist['name'])
        input(BreakLine('-'))
    elif op == 'v':
        selectedArtist = input('| Artist name > ').lower()
        artists = getArtists('', 'artists')
        succesfullSearch = False
        for artist in artists:
            if artist['name'].lower() == selectedArtist:
                cls(False)
                print(BreakLine('*') + '\n' + artist['name'].center(40) + '\n' + BreakLine('*'))
                foundArtist = getArtists(artist['id'],'artist')
                print('| Members:      ' + ', '.join(foundArtist['members']))
                print('| Genres:       ' + ', '.join(foundArtist['genres']))
                print('| Years active: ' + ' and '.join(foundArtist['years_active']))  
                input(BreakLine('-'))
                succesfullSearch = True
        if succesfullSearch == False:
            errorMessage(selectedArtist,'Artist not found')
    elif op == 'e':
        cls(False)
        break
    else:
        errorMessage(op, 'Unknown command')
        
input('SUCCESS: Script exited succesfully!')