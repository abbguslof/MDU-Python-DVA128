import json, requests

def list_artist():
    a = requests.get(
        'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/')
    artists, foundArtists = json.loads(a.text)['artists'], []
    for artist in artists:
        foundArtists.append((artist['name']))
    return foundArtists

def get_artist(name):
    a = requests.get(
        'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/')
    artists = json.loads(a.text)['artists']
    for artist in artists:
        try:
            if ((artist['name'].lower()) == name.lower()):
                foundArtist = get_artist_by_id(str(artist['id']))
                print('\n' + artist['name'].center(40) + '\n' + '-'*40)
                print('| Members:      ' + ', '.join(foundArtist['members']))
                print('| Genres:       ' + ', '.join(foundArtist['genres']))
                print('| Years active: ' + ' and '.join(foundArtist['years_active']))
        except:
            return (str(name) + ' is not a valid argument')
    else:
        return

def get_artist_by_id(id):
    a = requests.get(
        'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/' + id)
    artist = json.loads(a.text)['artist']
    return artist