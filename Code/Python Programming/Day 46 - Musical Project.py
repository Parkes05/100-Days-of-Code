import requests, os, spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth


user_input = input('which year do you what to travel to? Type the date in this format YYYY-MM-DD:\n')
year = user_input.split('-')[0]

response = requests.get(url=f'https://www.billboard.com/charts/hot-100/{user_input}/')
response.raise_for_status()
web_text = response.text

soup = BeautifulSoup(web_text, 'html.parser')
songs_list = [song.getText().strip() for song in soup.select('li h3')][0:100]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ['spotify_id'],
                                               client_secret=os.environ['spotify_code'],
                                               redirect_uri=os.environ['redirect'],
                                               scope='playlist-modify-private',
                                               show_dialog=True,
                                               cache_path="token.txt"))

song_urls = []
for song in songs_list:
    result = sp.search(type='track', q=f'track:{song} year:{year}')
    try:
        url = result['tracks']['items'][0]['external_urls']['spotify']
        song_urls.append(url)
    except:
        print(f"{song} doesn't exist in Spotify. Skipped.")
        
user_id = sp.current_user()['id']
playlist = sp.user_playlist_create(user=user_id, name=f'{user_input} Billboard 100', public=False)
sp.playlist_add_items(playlist_id=playlist['id'], items=song_urls)