import json
import time
from requests import ReadTimeout

MAX_REQUEST_ATTEMPTS = 5

def get_all_genres(artist_profiles):
    '''
    TODO
    '''
    genres = set()
    for artist in artist_profiles:
        for genre in artist['genres']:
            genres.add(genre)
    return genres

def get_artists_by_ids(user, artists):
    '''
    TODO
    '''
    artist_profiles = []
    for item in artists:
        artist = request_artist_from_api(user, (item['id']))
        if artist is not None:
            artist_profiles.append(artist)
    return artist_profiles

def request_artist_from_api(user, artist_id):
    try:
        return user.artist(artist_id)
    except ReadTimeout as e:
        print(f"artist id: {artist_id} | {e}")

def get_all_saved_tracks(user, limit_step=10, max_range=100):
    '''
    Gets a range of songs from the user's saved tracks and appends them to a list 
    '''
    tracks = []
    for offset in range(0, max_range, limit_step):
        response = user.current_user_saved_tracks(
            limit=limit_step,
            offset=offset,
        )
        if len(response) == 0:
            break
        tracks.extend(response['items'])

    return tracks

def get_all_artists(tracks):
    '''
    TODO
    '''
    artists = []
    for track in tracks:
        for artist in track['track']['artists']:
            artists.append(artist)

    # Returns a list with no duplicates
    return [i for n, i in enumerate(artists) if i not in artists[:n]]

def generate_genre_string_map(artist_nodes):
    genre_map = {}
    for artist in artist_nodes:
        for genre in artist.get_genres():
            if genre.get_name() not in genre_map:
                genre_map[genre.get_name()] = []
            if artist.get_name() not in genre_map[genre.get_name()]:
                genre_map[genre.get_name()].append(artist.get_name())
    return genre_map