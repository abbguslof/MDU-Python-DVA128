import os, requests, json
def cls(val):
    os.system('cls' if os.name=='nt' else 'clear')
    if val:
        print(breakline + "\n" + "Artist Database".center(40) + "\n" + breakline)
cls(False)
breakline = "-"*40
def getArtists(id,key):
    a = requests.get("https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/" + str(id))

    artists = json.loads(a.text)[key]
    return artists

def errorMessage(reason, instance):
    print(breakline + "\n| ERROR: " + instance + " '" + str(reason) + "' \n" + breakline)
    input("Press enter to continue")
    cls(True)

def printMenu():
    print("| L | List artists")
    print("| V | View artist profile")
    print("| E | Exit program")
    print(breakline)
print(breakline)
print("Artist Database".center(40))
print(breakline)
while True:
    printMenu()
    op = input("| Selection > ").lower().strip()
    if op in ["l", "v", "e"]:
        cls(True)
    if op == "l":
        artists = getArtists("", "artists")
        for artist in artists:
            print(artist["name"])
        print("*"*40)
    elif op == "v":
        selectedArtist = input("| Artist name > ").lower()
        artists = getArtists("", "artists")
        succesfullSearch = False
        for artist in artists:
            if artist["name"].lower() == selectedArtist:
                print("*"*40 + "\n" + artist["name"].capitalize().center(40) + "\n" + "*" *40)
                foundArtist = getArtists(artist["id"],"artist")
                print("| Members:      " + ", ".join(foundArtist["members"]))
                print("| Genres:       " + ", ".join(foundArtist["genres"]))
                print("| Years active: " + " ".join(foundArtist["years_active"]))  
                print(breakline)
                succesfullSearch = True
        if succesfullSearch == False:
            errorMessage(selectedArtist,"Artist not found")
    elif op == "e":
        cls(False)
        break
    else:
        errorMessage(op, "Unknown command")

print("SUCCES: Script exited succesfully!")
