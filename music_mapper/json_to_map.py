import json

from music_map import MusicMap

def build_map_from_json(input_file):
    with open(input_file, 'r') as file:
        tracks = json.load(file)
    
    data = []
    for track in tracks:
        artists = [artist['id'] for artist in track['track']['artists']]
        data = (track['track'], artists)
        
    map = MusicMap(data)
    return map


if __name__ == "__main__":
    input_file = 'data\mock_data\mock_track_data.json'
    nodes = build_map_from_json(input_file)

    pass