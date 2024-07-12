from spotipy.oauth2 import SpotifyOAuth 
from spotipy import Spotify

SCOPE = "user-library-read, user-follow-read"

class SPClient():
    def __init__(self, scope=SCOPE) -> None:
        self._sp_user = Spotify(auth_manager=SpotifyOAuth(scope=scope)) 
        self._tracks = self._get_user_saved_tracks()
        self._artists = self._get_all_artists_from_tracks(self._tracks)
        self._genres = self._get_genres(self._artists)
        
    def _get_user_saved_tracks(self, max_tracks=100):
        '''
        Gets a range of songs from the user's saved tracks and appends them to a list 
        '''
        tracks = []
        offset, limit = 0, 50
        while offset <= max_tracks:
            response = self._sp_user.current_user_saved_tracks(limit=limit, offset=offset)
            if len(response) == 0:
                break
            for item in response['items']:
                if item not in tracks:
                    tracks.append(item)
            offset += limit
        return tracks
    
    def _get_all_artists_from_tracks(self, tracks):
        '''
        TODO
        '''
        artist_ids = []
        for track in tracks:
            for artist in track['track']['artists']:
                artist_ids.append(artist['id'])
        return self._get_artists_by_ids(list(set(artist_ids)))
    
    def _get_artists_by_ids(self, artist_ids):
        artists = []
        if len(artist_ids) <= 50:
            return self._sp_user.artists([id for id in artist_ids])
        while len(artist_ids) > 50:
            artists += self._sp_user.artists([id for id in artist_ids[:50]])['artists']
            artist_ids = artist_ids[50:]
        return artists
    
    def _get_genres(self, artists):
        '''
        TODO
        '''
        genres = set()
        for artist in artists:
            for genre in artist['genres']:
                genres.add(genre)
        return genres