import json
from artist_data import *

class ArtistFactory:
    def create_object(self, data):
        # Process only the nested structures we want to keep as dictionaries
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, dict):
                    data[key] = value
                elif isinstance(value, list) and key == 'genres':
                    data[key] = [str(item) for item in value]
        return Artist(**data)

    def create_objects_from_json(self, json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)
            objects = []
            for item in data:
                obj = self.create_object(item)
                objects.append(obj)
            return objects