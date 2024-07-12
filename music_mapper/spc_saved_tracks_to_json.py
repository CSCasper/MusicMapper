from music_mapper.spc_client import SPClient
from music_mapper.music_map import MusicMap

import json

TRACKS_MAX_RANGE = 10000

if __name__ == "__main__":
    spc = SPClient()
    map = MusicMap()

    map.add_tracks(spc.get_user_saved_tracks(TRACKS_MAX_RANGE))
    
    data = {
        "Artists": map.Artists,
        "Tracks": map.Tracks,
        "Genres": map.Genres
    }
    
    json_data = json.dumps(data, indent=4)
    with open("data.json", "w") as file:
        file.write(json_data)