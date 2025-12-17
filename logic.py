from spotify_api import get_tracks_from_spotify
from youtube_api import create_youtube_playlist, search_youtube, add_video_to_playlist

def convert_playlist(sp_playlist_id, yt_playlist_name):
    tracks = get_tracks_from_spotify(sp_playlist_id)
    yt_id = create_youtube_playlist(yt_playlist_name)

    for t in tracks:
        query = f"{t['artist']} {t['name']}"
        video_id = search_youtube(query)
        if video_id:
            add_video_to_playlist(yt_id, video_id)

    return yt_id
