# YouTube Music Playlist Automation

Automate the process of adding songs to a YouTube Music playlist using the YouTube Data API.

## Prerequisites

Before running the script, ensure you have the following:

- Python installed (version 3.6 or higher)
- Required Python libraries installed. Install them using:

    ```bash
  pip install pandas google-auth-oauthlib google-auth google-api-python-client
    ```

- YouTube API client secrets: Obtain this from the Google Cloud Console.

## Setup

1. Clone/download the repository and navigate into it in your terminal.


    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```
2. Download the `credentials.json` file provided by Google for OAuth2 authentication with the YouTube Data API

3. Add your CSV file:
     Replace 'your_file.csv' with the actual file path containing the song data.

4. Add your YouTube API client secrets:
    Replace CLIENT_SECRETS_FILE = '' with the actual path to your YouTube API client secrets JSON file.

5. Specify the YouTube Music playlist ID:
    Replace playlist_id = '' with the ID of the YouTube Music playlist where you want to add the songs.

##  Usage

To run the script, by executing the following command:

```
    python scripts.py
```
The script will iterate through the CSV file, search for each song on YouTube, and add it to the specified playlist.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests.

## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/licenses/MIT)
page for details

### Happy  coding!


