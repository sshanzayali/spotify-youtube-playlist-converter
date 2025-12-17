import json
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

CLIENT_SECRET_FILE = os.getenv("GOOGLE_CLIENT_SECRET_FILE", "client_secret.json")

youtube = None

# load search cache
CACHE_FILE = "yt_cache.json"
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "r") as f:
        search_cache = json.load(f)
else:
    search_cache = {}


def get_youtube_service():

    global youtube

    if youtube is None:
        flow = InstalledAppFlow.from_client_secrets_file(
            CLIENT_SECRET_FILE,
            scopes=["https://www.googleapis.com/auth/youtube"]
        )

        credentials = flow.run_local_server(port=0)
        youtube = build('youtube', 'v3', credentials=credentials)

    return youtube


def save_cache():
    with open(CACHE_FILE, "w") as f:
        json.dump(search_cache, f, indent=2)


def create_youtube_playlist(title, description=""):
    yt = get_youtube_service()

    request = yt.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {"title": title, "description": description},
            "status": {"privacyStatus": "private"}
        }
    )
    response = request.execute()
    return response["id"]


def search_youtube(query):
    yt = get_youtube_service()

    # check cache first
    if query in search_cache:
        return search_cache[query]

    request = yt.search().list(
        part="snippet",
        q=query,
        maxResults=1,
        type="video"
    )
    response = request.execute()

    if response["items"]:
        video_id = response["items"][0]["id"]["videoId"]
        search_cache[query] = video_id
        save_cache()
        return video_id

    search_cache[query] = None
    save_cache()
    return None


def add_video_to_playlist(playlist_id, video_id):
    yt = get_youtube_service()

    request = yt.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": playlist_id,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": video_id
                }
            }
        }
    )
    return request.execute()
