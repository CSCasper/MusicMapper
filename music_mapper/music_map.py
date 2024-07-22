import json

from mapper_nodes.mapper_node import TrackNode, ArtistNode, GenreNode
from mapper_nodes import track_data as td
from mapper_nodes import artist_data as ad

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
    
    def add_tracks(self, tracks, get_artists=False):
        # Add tracks to the map
        for i in range(len(tracks)):
            t_data = td.Track.from_dict(tracks[i][0])
            if t_data.id not in self.Tracks:
                self.Tracks[t_data.id] = TrackNode(t_data.name, t_data.artists, t_data.id, tracks[i][0])
            # Add artists to the map if requested
            if get_artists:
                self.add_artists(tracks[i][1])
        # Refresh artist connections to tracks
        # TODO add connection between artists if they're on the same track
        self._add_artist_connections()
                    
    def add_artists(self, artists):
        for i in range(len(artists)):
            a_data = ad.Artist.from_dict(artists[i])
            if a_data.id not in self.Artists:
                self.Artists[a_data.id] = ArtistNode(a_data.name, a_data.genres, a_data.id, artists[i])

    def _add_artist_connections(self):
        track_ids = self.Tracks.keys()
        artist_ids = self.Artists.keys()
        
        # Add connections between artists and tracks
        # TODO figure out a way to do this quicker
        # TODO generate GenreNodes from artist genres
        for artist_id in artist_ids:
            for track_id in track_ids:
                if self.Tracks[track_id].has_artist(artist_id):
                    self.Artists[artist_id].add_connection(self.Tracks[track_id])

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

    