'''Test file for spotipy'''

import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SCOPE = "user-library-read,user-follow-read"
TRACKS_MAX_RANGE = 100

def main():
    '''
    TODO
    '''
    sp_user = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))

    user_tracks     = get_all_saved_tracks(sp_user, max_range=TRACKS_MAX_RANGE)
    user_artists    = get_all_artists(user_tracks)
    artist_profiles = get_artists_by_ids(sp_user, user_artists)

    genres = get_all_genres(artist_profiles)

    for genre in sorted(genres):
        print(genre)

    print_artists(user_artists)
    # dump_tracks_to_json(user_tracks)
    # print_tracks(user_tracks)

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
        artist_profiles.append(user.artist(item['id']))
    return artist_profiles

def get_all_saved_tracks(user, limit_step=50, max_range=100):
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

def dump_tracks_to_json(tracks):
    '''
    TODO
    '''
    with open('result.json', 'w' ,encoding='utf-8') as fp:
        json.dump(tracks, fp, indent=4)

def print_tracks(tracks):
    '''
    Print a list of tracks
    '''
    for idx, track in enumerate(tracks):
        print(idx, track['track']['artists'][0]['name'], " – ", track['track']['name'])

def print_artists(artists):
    '''
    TODO
    '''
    for idx, artist in enumerate(sorted(artists, key=lambda d: d['name'])):
        print(idx, artist['name'])

main()
