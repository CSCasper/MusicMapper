import json

from mapper_nodes import artist_data
from mapper_nodes.mapper_node import TrackNode, ArtistNode, GenreNode
from mapper_nodes import track_data

class MusicMap():
    
    def __init__(self) -> None:
        self.Tracks = {}
        self.Artists = {}
        self.Genres = {}  
    
    def _get_genres_from_artists(self):
        genre_lists = [artist.get_genres() for artist in self.Artists]
        return [GenreNode(genre) for genres in genre_lists for genre in genres]
        
    def _refresh_genres(self):
        self.Genres = set()
        self.Genres.update(self._get_genres_from_artists())
    
    def _nodes_to_dict(self): 
        node_dict = { "Artists": {}, "Tracks": {}, "Genres": {} }
        for k,v in self.Artists.items():
            node_dict["Artists"][k] = v.to_dict()
        for k,v in self.Tracks.items():
            node_dict["Tracks"][k] = v.to_dict()
        for k,v in self.Genres.items():
            node_dict["Genres"][k] = v.to_dict()    
        return node_dict
    
    def add_tracks(self, tracks):
        for i in range(len(tracks)):
            t_data = track_data.Track.from_dict(tracks[i][0])
            if t_data.id not in self.Tracks:
                self.Tracks[t_data.id] = TrackNode(t_data.name, t_data.artists, t_data.id, tracks[i][0])
            for j in range(len(tracks[i][1])):
                a_data = artist_data.Artist.from_dict(tracks[i][1][j])
                if a_data.id not in self.Artists:
                    self.Artists[a_data.id] = ArtistNode(a_data.name, a_data.genres, a_data.id, tracks[i][1][j])
                self.Artists[a_data.id].add_connection(self.Tracks[t_data.id])
    
    def nodes_to_json(self):
        return json.dumps(self._nodes_to_dict(), indent=4)
    
    def print_artist_tracks(self):
        for artist in self.Artists.values():
            tracks = [node for node in artist.get_connections() if type(node) is TrackNode]
            print(f"Artist: {artist.get_name()}")
            for track in tracks:
                print(f"|__ Track: {track.get_title()}")
            print()

    def get_all_nodes(self):
        return list(self.Tracks) + list(self.Artists) + list(self.Genres)

    