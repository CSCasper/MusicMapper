'''Test file for spotipy'''

from MusicMapper.sp_client import SPClient

from MusicMapper.artist_node_factory import *
from MusicMapper.artist_data import *

import json

data_dump_dir = "./data/out"

TRACKS_MAX_RANGE = 50

def main():
    spc = SPClient()

    # formatted_date = datetime.now().strftime("%d%m%Y-%H%M%S")
    # formatted_file_name = data_dump_dir + formatted_date + ".json"
    
    # # Write the dictionary to a JSON file
    # with open(formatted_file_name, 'w') as json_file:
    #     json.dump(user_artists_by_id, json_file, indent=4)

    # print(f"Dictionary has been exported to {data_dump_dir}/")

    # # Create the factory
    # factory = ArtistFactory()
    # # Create objects from the JSON file
    # artists = factory.create_objects_from_json(formatted_file_name)
    pass
    
main()
