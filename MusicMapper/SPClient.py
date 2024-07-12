from spotipy.oauth2 import SpotifyOAuth 
from spotipy import Spotify

SCOPE = "user-library-read, user-follow-read"

class SPClient():
    def __init__(self, scope=SCOPE) -> None:
        self._sp_user = Spotify(auth_manager=SpotifyOAuth(scope=scope)) 
        
    def get_user_saved_tracks(self, max_tracks=100):
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
                artists = self._get_artists_by_ids([artist['id'] for artist in item['track']['artists']])
                tracks.append((item['track'], artists))
            offset += limit
        return tracks
    
    def _get_all_artists_from_tracks(self, tracks):
        '''
        TODO
        '''
        artist_ids = []
        for track in tracks:
            for artist in track['artists']:
                artist_ids.append(artist['id'])
        return self._get_artists_by_ids(list(set(artist_ids)))
    
    def _get_artists_by_ids(self, artist_ids):
        artists = []
        if len(artist_ids) <= 50:
            return self._sp_user.artists([id for id in artist_ids])['artists']
        while len(artist_ids) > 50:
            artists += self._sp_user.artists([id for id in artist_ids[:50]])['artists']
            artist_ids = artist_ids[50:]
        return artists