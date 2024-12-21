import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from config.config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

auth_manager = SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
)
spotify = spotipy.Spotify(auth_manager=auth_manager)

def search_song(query):
    results = spotify.search(q=query, type="track", limit=1)
    if results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        return {
            "name": track["name"],
            "artist": ", ".join(artist["name"] for artist in track["artists"]),
            "url": track["external_urls"]["spotify"],
            "thumbnail": track["album"]["images"][0]["url"],
            "preview_url": track.get("preview_url")
        }
    return None

def get_playlist(playlist_url):
    playlist_id = playlist_url.split("/")[-1].split("?")[0]
    results = spotify.playlist_tracks(playlist_id)
    return [
        {
            "name": track["track"]["name"],
            "artist": ", ".join(artist["name"] for artist in track["track"]["artists"]),
            "url": track["track"]["external_urls"]["spotify"],
            "thumbnail": track["track"]["album"]["images"][0]["url"]
        }
        for track in results["items"]
  ]
  
