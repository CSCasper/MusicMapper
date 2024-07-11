'''Test file for spotipy'''

import pprint as pp
import spotipy

from artist_node_factory import *
from artist_data import *

from spotipy.oauth2 import SpotifyOAuth

from dataplay import *

from datetime import datetime

import json

data_dump_dir = "./data/out"

SCOPE = "user-library-read,user-follow-read"
TRACKS_MAX_RANGE = 5

def main():
    sp_user = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))

    user_tracks = get_all_saved_tracks(sp_user, max_range=TRACKS_MAX_RANGE)
    user_artists = get_all_artists(user_tracks)
    user_artists_by_id = get_artists_by_ids(sp_user, user_artists)

    formatted_date = datetime.now().strftime("%d%m%Y-%H%M%S")
    formatted_file_name = data_dump_dir + formatted_date + ".json"
    
    # Write the dictionary to a JSON file
    with open(formatted_file_name, 'w') as json_file:
        json.dump(user_artists_by_id, json_file, indent=4)

    print(f"Dictionary has been exported to {data_dump_dir}")

    # Create the factory
    factory = ArtistFactory()
    # Create objects from the JSON file
    artists = factory.create_objects_from_json(formatted_file_name)
    
main()
