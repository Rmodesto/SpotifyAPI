# app.py
from flask import Flask, redirect, request
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)

@app.route('/')
def index():
    sp_oauth = SpotifyOAuth(client_id='your_client_id',
                            client_secret='your_client_secret',
                            redirect_uri='http://localhost:8000/callback',
                            scope='user-library-read')
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    sp_oauth = SpotifyOAuth(client_id='your_client_id',
                            client_secret='your_client_secret',
                            redirect_uri='http://localhost:8000/callback',
                            scope='user-library-read')
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    access_token = token_info['access_token']
    return f"Access token: {access_token}"

if __name__ == "__main__":
    app.run(port=8000)
