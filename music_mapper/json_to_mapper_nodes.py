import json

from music_mapper.music_map import MusicMap

def build_nodes_from_json(input_file):
    with open(input_file, 'r') as file:
        data = json.load(file)

    map = MusicMap(data)

    return nodes


if __name__ == "__main__":
    input_file = 'data\out11072024-101102.json'
    nodes = build_nodes_from_json(input_file)

    pass