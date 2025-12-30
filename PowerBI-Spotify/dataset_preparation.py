import requests
import pandas as pd

# Function to get Spotify the access token
def get_spotify_token(client_id, client_secret):
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(auth_url, {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    })
    auth_data = auth_response.json()
    return auth_data['access_token']

# Function to search for a track and get its ID
def search_track(track_name, artist_name, token):
    query = f"{track_name} artist:{artist_name}"
    url = f"https://api.spotify.com/v1/search?q={query}&type=track"
    response = requests.get(url, headers={
    'Authorization': f'Bearer {token}'
    })
    json_data = response.json()
    try:
        first_result = json_data['tracks']['items'][0]
        track_id = first_result['id']
        return track_id
    except (KeyError, IndexError):
        return None

# Function to get track details:
def get_track_details(track_id, token):
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    response = requests.get(url, headers={
        'Authorization': f'Bearer {token}'
        })
    json_data = response.json()
    image_url = json_data['album']['images'][0]['url']
    return image_url

# Spotify API credentials
client_id = 'f4585ec4a6cd4ff69cb29cdc58cfd165'
client_secret = 'd576bb355fde48d5a4e897f7f586cada'

# Get Access Token 
access_token = get_spotify_token(client_id, client_secret)

# Load the dataset
df_spotify = pd.read_csv('spotify-2023.csv', encoding='ISO-8859-1')

# Prepare to store image URLs
df_spotify['image_url'] = None

# Loop through each row to get track details and add to DataFrame
for i, row in df_spotify.iterrows():
    try:
        track_id = search_track(row['track_name'], row['artist(s)_name'], access_token)
        if track_id:
            image_url = get_track_details(track_id, access_token)
            df_spotify.at[i, 'image_url'] = image_url
        print(f"Processed {i+1}/{len(df_spotify)} rows.", end='\r')
    except Exception as e:
        print(f"Error processing row {i}: {e}")

# Save the updated Dataset 
df_spotify.to_csv('final-spotify-2023.csv', index=False)