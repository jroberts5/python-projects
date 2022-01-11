import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100"
SPOTIFY_CLIENT_ID = os.environ['SPOTIFY_CLIENT_ID']
SPOTIFY_CLIENT_SECRET = os.environ['SPOTIFY_CLIENT_SECRET']
REDIRECT_URI = "http://127.0.0.1:5500/"
sp_scope = "playlist-modify-private"


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = date.split("-")[0]


# Scrapes Billboard100 into list of billboard songs
website_html = requests.get(url=f"{BILLBOARD_URL}/{year}").text
soup = BeautifulSoup(website_html, "html.parser")
chart_songs = soup.find_all(name="span", class_="chart-element__information__song")
song_list = [song.get_text() for song in soup.find_all(name="span", class_="chart-element__information__song")]


spotify_oauth = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=sp_scope,
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
    )
)

user_id = sp.current_user()["id"]
print(user_id)

#Searching Spotify for songs by title
song_uris = []
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)