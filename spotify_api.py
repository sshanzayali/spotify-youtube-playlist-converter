import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_uri="http://127.0.0.1:8000/callback",
    scope="playlist-read-private"
))


def get_user_playlists():
    return sp.current_user_playlists()


def extract_playlist_id(playlist_input):
    if "spotify.com" in playlist_input:
        return playlist_input.split("/playlist/")[1].split("?")[0]
    return playlist_input

def get_tracks_from_spotify(playlist_id):
    tracks = []

    # loop until no more tracks
    results = sp.playlist_tracks(playlist_id)
    items = results["items"]

    while results["next"]:
        results = sp.next(results)
        items.extend(results["items"])

    # clean data
    for item in items:
        track = item["track"]

        if track is None:
            continue

        track_name = track["name"]
        artist_name = track["artists"][0]["name"]  # primary artist

        tracks.append({
            "name": track_name,
            "artist": artist_name
        })

    return tracks
