def load_credentials():
    with open('credentials.txt', 'r') as f:
        lines = f.readlines()
        id = lines[0].strip()
        secret = lines[1].strip()
    return id, secret

SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET = load_credentials()
