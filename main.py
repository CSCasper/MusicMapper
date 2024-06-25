'''Test file for spotipy'''

import pprint as pp
import spotipy
import node
from spotipy.oauth2 import SpotifyOAuth

from dataplay import *


SCOPE = "user-library-read,user-follow-read"
TRACKS_MAX_RANGE = 10

def main():
    '''
    TODO
    '''
    node_1 = node.Node()
    node_2 = node.Node()
    node_3 = node.GenreNode()

    node_1.add_connection(node_2)
    node_3.add_connection(node_2)

    sp_user = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))

    user_tracks = get_all_saved_tracks(sp_user, max_range=TRACKS_MAX_RANGE)
    user_artists = get_all_artists(user_tracks)
    user_artists_by_id = get_artists_by_ids(sp_user, user_artists)

    pp.pprint(user_tracks)
    pp.pprint(user_artists)
    pp.pprint(user_artists_by_id)

main()
