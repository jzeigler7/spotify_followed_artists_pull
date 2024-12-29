import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Spotify API credentials from .env
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

# Spotify OAuth scopes for accessing followed artists
SCOPE = "user-follow-read"

def fetch_followed_artists():
    # Authenticate with Spotify
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE
    ))

    # Fetch followed artists
    print("Fetching your followed artists...")
    followed_artists = []
    next_cursor = None  # Cursor for pagination

    while True:
        # Get current batch of followed artists
        results = sp.current_user_followed_artists(limit=20, after=next_cursor)
        artists = results['artists']['items']
        followed_artists.extend(artists)

        # Check if there are more artists to fetch
        next_cursor = results['artists']['cursors'].get('after')
        if not next_cursor:
            break

    # Display followed artists as a numbered list
    for index, artist in enumerate(followed_artists, start=1):
        print(f"{index}. {artist['name']}")

    print(f"Total followed artists: {len(followed_artists)}")
    return followed_artists

if __name__ == "__main__":
    fetch_followed_artists()
