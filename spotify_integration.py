import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyIntegration:
    def __init__(self, client_id, client_secret):
        self.sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

    def get_track_info(self, url):
        track_info = self.sp.track(url)
        track_name = track_info['name']
        track_artist = track_info['artists'][0]['name']
        return f"{track_name} by {track_artist}"