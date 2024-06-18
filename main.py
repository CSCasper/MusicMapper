'''Test file for spotipy'''

import spotipy
import pprint
from spotipy.oauth2 import SpotifyOAuth

from dataplay import *
from node import TrackNode, ArtistNode, GenreNode

SCOPE = "user-library-read,user-follow-read"
TRACKS_MAX_RANGE = 100

def main():
    '''
    TODO
    '''
    sp_user = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))

    user_tracks  = get_all_saved_tracks(sp_user, max_range=TRACKS_MAX_RANGE)
    user_artists = get_all_artists(user_tracks)
    
    user_artists_by_id = get_artists_by_ids(sp_user, user_artists)

    track_nodes = []
    artist_nodes = []
    
    for track in user_tracks:
        track_artists = track['track']['artists']
        curr_artist_nodes = []
        for artist in track_artists:
            curr_artist_id = find_matching_artist(artist['name'], user_artists_by_id)
            curr_artist_node = ArtistNode(artist['name'],
                                          create_genre_nodes(curr_artist_id['genres']))
            artist_nodes.append(curr_artist_node)
            curr_artist_nodes.append(curr_artist_node)
        curr_track_node = TrackNode(track['track']['name'], curr_artist_nodes)
        track_nodes.append(curr_track_node)

    genre_map = generate_genre_string_map(artist_nodes)
    pprint.pprint(genre_map)

def find_matching_artist(artist_name, artists_by_id):
    for artist in artists_by_id:
        if artist_name == artist['name']:
            return artist
    raise Exception('artist id not found')

def create_genre_nodes(genres):
    genre_nodes = []
    for genre in genres:
        genre_nodes.append(GenreNode(genre))
    return genre_nodes

def generate_genre_string_map(artist_nodes):
    genre_map = {}
    for artist in artist_nodes:
        for genre in artist.get_genres():
            if genre.get_name() not in genre_map:
                genre_map[genre.get_name()] = []
            if artist not in genre_map[genre.get_name()]:
                genre_map[genre.get_name()].append(artist.get_name())
    return genre_map
            
main()