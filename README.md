
<h1 align="center">
  <br>
  <img src="https://github.com/user-attachments/assets/f331bcfd-5267-49fd-84dc-fea592988bac" alt="logo" width="300">


 
  <br>
  Spotify → YouTube Playlist Converter
  <br>
</h1>

<h4 align="center">An easy-to-use automated YouTube playlist maker</h4>

<p align="center">
  
  <a href="https://www.linkedin.com/in/shanzaya/">
    <img src="https://img.shields.io/badge/-LinkedIn-blue?style=flat">
  </a>
  
</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#credits">Credits</a> •
  <a href="#links">Links</a>

  
![demo1](https://github.com/user-attachments/assets/41e71949-d582-42e6-ad05-70abb5a9f681)


</p>


## Key Features

* Automatically converts Spotify playlists into YouTube playlists
* Utilises Spotify Web API to fetch playlist tracks
* Utilises YouTube Data API to create the playlists + add videos
* Desktop GUI, built with Tkinter (no browser UI required)
* OAuth authentication for Spotify and Google


## How To Use


### 1. Clone the repository
git clone [https://github.com/sshanzayali/spotify-youtube-playlist-converter.git](https://github.com/sshanzayali/spotify-youtube-playlist-converter.git)
```bash
cd spotify-youtube-playlist-converter
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Spotify API setup
Create a <a href="https://developer.spotify.com/documentation/web-api/concepts/apps">Spotify Developer app</a> and add the following Redirect URI:
http://127.0.0.1:8000/callback

Create a `.env` file in the project root:

```bash
SPOTIFY_CLIENT_ID=your_id_here
SPOTIFY_CLIENT_SECRET=your_secret_here
```

### 4. Google API setup
Create a Google OAuth **Desktop App**.
Download `client_secret.json` and place it in the project root.

### 5. Run the application
python gui.py

### 6. Convert a playlist
- Paste a Spotify playlist URL
- Enter a YouTube playlist name  
- Click "Convert Playlist"


## Credits
Built using:
* Spotify Web API
* Youtube Data API v3
* Spotipy
* Google API Python Client
* Tkinter


## Links

---
> GitHub [@sshanzayali](https://github.com/sshanzayali) &nbsp;&middot;&nbsp;
> LinkedIn [Shanzay Ali](https://www.linkedin.com/in/shanzaya/)

