from spotipy.oauth2 import SpotifyOAuth 
from spotipy import Spotify
import time

SCOPE = "user-library-read, user-follow-read"

class SPClient():
    def __init__(self, scope=SCOPE) -> None:
        self._sp_user = Spotify(auth_manager=SpotifyOAuth(scope=scope)) 
        
    def get_user_saved_tracks(self, max_tracks=100):
        '''
        Gets a range of songs from the user's saved tracks and appends them to a list 
        '''
        # TODO simplify or omit variables
        # TODO fix max_tracks so it is exact
        # TOOD add feature to get all tracks elegantly
        tracks = []
        track_data = []
        known_artist_profiles = {}
        offset = 0
        
        limit = 50 if max_tracks > 50 else max_tracks
        
        while offset <= max_tracks:
            response = self._sp_user.current_user_saved_tracks(limit=limit, offset=offset)
            if len(response) == 0:
                break
            track_data += response['items']
            offset += limit
            
        for item in track_data:
            for artist in item['track']['artists']:
                if artist['id'] not in known_artist_profiles:
                    known_artist_profiles[artist['id']] = None
        
        artists = self._get_artists_by_ids(list(known_artist_profiles.keys()))
        
        for track in track_data:
            track_artists = [artists[artist['id']] for artist in track['track']['artists']]
            tracks.append((track['track'], track_artists))
        
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
        ids = artist_ids.copy()
        if len(ids) <= 50:
            artists = self._sp_user.artists([id for id in ids])['artists']    
        else:  
            while len(ids) > 0:
                artists += self._sp_user.artists([id for id in ids[:50]])['artists']
                ids = ids[50:]
        return dict(zip(artist_ids, artists))