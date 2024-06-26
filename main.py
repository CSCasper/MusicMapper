'''Test file for spotipy'''

import pprint as pp
import spotipy
import mapper_node

from artist_node_factory import *
from artist_data import *

from spotipy.oauth2 import SpotifyOAuth

from dataplay import *

import json

data_dump = "./data/mock_data/out.json"

SCOPE = "user-library-read,user-follow-read"
TRACKS_MAX_RANGE = 10

def main():
    # node_1 = mapper_node.Node()
    # node_2 = mapper_node.Node()
    # node_3 = mapper_node.GenreNode()

    # node_1.add_connection(node_2)
    # node_3.add_connection(node_2)

    sp_user = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))

    user_tracks = get_all_saved_tracks(sp_user, max_range=TRACKS_MAX_RANGE)
    user_artists = get_all_artists(user_tracks)
    user_artists_by_id = get_artists_by_ids(sp_user, user_artists)

    # Write the dictionary to a JSON file
    with open(data_dump, 'w') as json_file:
        json.dump(user_artists_by_id, json_file, indent=4)

    print(f"Dictionary has been exported to {data_dump}")

    # Create the factory
    factory = ArtistFactory()

    # Create objects from the JSON file
    artists = factory.create_objects_from_json(data_dump)

    pp.pprint(artists)
    # pp.pprint(user_tracks)
    # pp.pprint(user_artists)
    # pp.pprint(user_artists_by_id)

main()
