from music_mapper.mapper_nodes import artist_data
from music_mapper.mapper_nodes.mapper_node import TrackNode, ArtistNode, GenreNode
from music_mapper.mapper_nodes import track_data

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
    
    def add_tracks(self, tracks):
        for i in range(len(tracks)):
            t_data = track_data.Track.from_dict(tracks[i][0])
            if t_data.id not in self.Tracks:
                self.Tracks[t_data.id] = TrackNode(t_data.name, t_data.artists, t_data.id)
            for j in range(len(tracks[i][1])):
                a_data = artist_data.Artist.from_dict(tracks[i][1][j])
                if a_data.id not in self.Artists:
                    self.Artists[a_data.id] = ArtistNode(a_data.name, a_data.genres, a_data.id)
                self.Artists[a_data.id].add_connection(self.Tracks[t_data.id])
        
    def print_artist_tracks(self):
        for artist in self.Artists.values():
            tracks = [node for node in artist.get_connections() if type(node) is TrackNode]
            print(f"Artist: {artist.get_name()}")
            for track in tracks:
                print(f"|__ Track: {track.get_title()}")
            print()

    def get_all_nodes(self):
        return list(self.Tracks) + list(self.Artists) + list(self.Genres)

    