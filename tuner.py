import time
import webbrowser
import tkinter as tk
from tkinter import simpledialog
# from PIL import Image, ImageTk
import datetime
import requests

API_KEY = 'dc223d0162eed54cacd81a581a219b44'  # Our API key
API_SECRET = '588fcc02dfb549a295139437e4b78477' # Our API secrets

date = datetime.date.today() # Gets the date
realDate = date.strftime("%B %d, %Y") # Formats the date

print(f"Today is {realDate}") # Prints out the date
username = input("Enter your Last.fm username: ") # Asks for the users username
print(f"Hey {username}, check out your top tunes!") # Prints a welcome message


def fetch_song_details(username): # This fetches the details from the top song, using the username as a parameter
    url = f"http://ws.audioscrobbler.com/2.0/?method=user.getRecentTracks&user={username}&api_key={API_KEY}&format=json&limit=1" # Connects with the lastFM api to get the details
    response = requests.get(url).json() # Response, duh

    if 'recenttracks' not in response or len(response['recenttracks']['track']) == 0:
        return None # If there are no recent tracks

    track = response['recenttracks']['track'][0]
    song_name = track['name'] # this is the name of the song
    artist_name = track['artist']['#text'] # this is the name of the artist
    album_cover_url = track['image'][-1]['#text'] # this is the cover that we download and show in the popup
    track_url = track['url'] # this is the url

    return song_name, artist_name, album_cover_url, track_url

def display_recent_track(username):
    try:
        result = fetch_song_details(username)
        if result is None:
            print(f"No recent tracks found for {username}.")
        else:
            song_name, artist_name, album_cover_url, track_url = result
            print(f"Most Recent Song: '{song_name}' by {artist_name}")
            
    except Exception as e:
        print(f"Error: {str(e)}")

def fetch_top_tracks(username): # This gets our top tracks from the API
    url = f"http://ws.audioscrobbler.com/2.0/?method=user.getTopTracks&user={username}&api_key={API_KEY}&format=json&period=7day&limit=5"
    response = requests.get(url).json()

    if 'toptracks' not in response or len(response['toptracks']['track']) == 0:
        return None

    tracks = response['toptracks']['track']
    top_songs = [(track['name'], track['artist']['name']) for track in tracks]
    return top_songs

def display_top_tracks(username): # This displays our top tracks
    try:
        top_songs = fetch_top_tracks(username)
        if top_songs is None:
            print(f"No top tracks found for {username} this week.")
        else:
            print(f"Top 5 Tracks for {username} (Past 7 Days):")
            for i, (song, artist) in enumerate(top_songs, 1):
                print(f"{i}. '{song}' by {artist}")
    except Exception as e:
        print(f"Error: {str(e)}")

# Run the functions
display_recent_track(username)
display_top_tracks(username)
print(f"""Goodbye, {username}!""")