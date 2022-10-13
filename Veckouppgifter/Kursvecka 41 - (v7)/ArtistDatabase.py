import json, requests

def list_artist():
    """
    Get all Arists

    @return: List of artists
    """
    a = requests.get(
        'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/')
    artists, foundArtists = json.loads(a.text)['artists'], []
    for artist in artists:
        foundArtists.append((artist['name']))
    return foundArtists

def get_artist(name):
    """
    Get an artist by their name

    @param Name of the Artist: String
    @return: Artist dictionary
    """
    artists = requests.get(
        'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/').json()['artists']
    for artist in artists:
            if ((artist['name'].lower()) == name.lower()):
                _artist = get_artist_by_id(artist['id'])
                _artist['name'] = artist['name']
                return _artist

def get_artist_by_id(id):
    """
    Get an artist by their ID

    @param ID of the Artist: String
    @return: 
    """
    artist = requests.get('https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/' + id).json()['artist']
    artist['id'] = id
    return artist