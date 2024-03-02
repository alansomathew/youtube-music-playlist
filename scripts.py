import os
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
import pandas as pd

# Load CSV data (replace 'your_file.csv' with the actual file path)
df = pd.read_csv('')

# Replace 'your_youtube_client_secrets.json' with your actual client secrets file
CLIENT_SECRETS_FILE = ''

# Specify the YouTube Music playlist ID
playlist_id = ''

# Function to get the YouTube Music API service
def get_youtube_service(client_secrets_file):
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, ['https://www.googleapis.com/auth/youtube.force-ssl']
    )
    credentials = flow.run_local_server(port=0)
    return build('youtube', 'v3', credentials=credentials)


# Function to search for a song and add it to the playlist
def search_and_add_song(youtube, track_name, artist_name):
    query = f'{track_name} {artist_name} official music video'
    search_response = youtube.search().list(
        q=query,
        part='id',
        type='video',
        maxResults=1
    ).execute()

    if 'items' in search_response:
        video_id = search_response['items'][0]['id']['videoId']
        youtube.playlistItems().insert(
            part='snippet',
            body={
                'snippet': {
                    'playlistId': playlist_id,
                    'position': 0,
                    'resourceId': {
                        'kind': 'youtube#video',
                        'videoId': video_id
                    }
                }
            }
        ).execute()
        print(f"Added '{track_name} - {artist_name}' to the playlist.")
    else:
        print(f"Could not find '{track_name} - {artist_name}' on YouTube.")

# Main function
def main():
    youtube = get_youtube_service(CLIENT_SECRETS_FILE)

    for index, row in df.iterrows():
        track_name = row['Track name']
        print(track_name)
        artist_name = row['Artist name']
        search_and_add_song(youtube, track_name, artist_name)

if __name__ == '__main__':
    main()
