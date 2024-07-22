from datetime import datetime
from spc_client import SPClient
from music_map import MusicMap

TRACKS_MAX_RANGE = 10000

def main():
    spc = SPClient()
    map = MusicMap()

    map.add_tracks(spc.get_user_saved_tracks(TRACKS_MAX_RANGE), True)
    
    now = datetime.now().strftime("%m%d%y-%H%M%S")
    
    json_data = map.nodes_to_json()
    with open(f"data_{now}.json", "w") as file:
        file.write(json_data)
        
main()