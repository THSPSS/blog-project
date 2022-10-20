import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from bs4 import BeautifulSoup
import requests


ID="6d67ca8f2ed0495db6e6d03b6369f6e3"
SECRET ="8a81b603e5a14848a4bb03244cb8be7c"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=ID,
        client_secret=SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
#input_day = input("Which year do you want to travel to? Type date in this format YYYY-MM-DD:")
input_day = "2001-08-10"
print(input_day)


response = requests.get("https://www.billboard.com/charts/hot-100/" + input_day)

soup = BeautifulSoup(response.text,"html.parser")
songs = [song.getText() for song in soup.select(selector=".o-chart-results-list__item .c-title")]


song_uris = []
year = input_day.split("-")[0]
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")



playlist = sp.user_playlist_create(user=user_id, name=f"{input_day} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)