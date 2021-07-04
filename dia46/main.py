from datetime import datetime
from os import name
import requests
from bs4 import BeautifulSoup

# data = input('Seleccione el año (YYYY-MM-DD): ')
data = '1991-08-29'

url = f'https://www.billboard.com/charts/hot-100/{data}'


response = requests.get(url=url)
info = response.text

soup = BeautifulSoup(info, 'html.parser')
titles = soup.find_all(name='span', class_='chart-element__information__song')
my_playlist = [title.getText() for title in titles]

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id="ed7aa4a1a9c74f1487adaab6ccc5fe7c",
        client_secret="6871ef4c5b6c492fa50c0e32f8fca0c2",
        redirect_uri="http://127.0.0.1:5500/",
        scope="playlist-modify-private"
    )
)
song_uri = []
user = sp.current_user()["id"]
year = data.split('-')[0]
for song in my_playlist:
     res = sp.search(q=f"track:{song} year:{year}", type='track')
    #  print(res)
     try:
        uri = res["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
     except IndexError:
        print(f"{song} no existe")
    
playlist =sp.user_playlist_create(user=user, name=f"Billboard {year}", public=False)
sp.playlist_add_items(playlist_id=playlist['id'], items=song_uri)