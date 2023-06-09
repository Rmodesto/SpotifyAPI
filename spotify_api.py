import os

import pandas as pd
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials

# Load environment variables from .env file
load_dotenv()

# Initialize SpotiPy with user credentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.environ.get('SPOTIPY_CLIENT_ID'),
    client_secret=os.environ.get('SPOTIPY_CLIENT_SECRET')
))

def get_top_songs():
    genre = input("Enter a genre: ")

    results = sp.search(q=f'genre:"{genre}"', type='playlist', limit=10)
    song_data = []
    
    for playlist in results['playlists']['items']:
        tracks = sp.playlist(playlist['id'], additional_types=('track',))
        for item in tracks['tracks']['items']:
            if 'track' in item:
                track = item['track']
                song_data.append({
                    'name': track['name'],
                    'artist': track['artists'][0]['name'],
                    'id': track['id']
                })
    
    song_data = pd.DataFrame(song_data)
    
    # Ensure we only get the top 100 songs
    if len(song_data) > 100:
        song_data = song_data.sample(n=100)

    # Get the BPM and key for each song
    for idx, row in song_data.iterrows():
        features = sp.audio_features(row['id'])[0]
        song_data.at[idx, 'bpm'] = features['tempo']
        song_data.at[idx, 'key'] = features['key']

    return song_data

# Usage
top_songs = get_top_songs()
print(top_songs)
