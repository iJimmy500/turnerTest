import time
import webbrowser
import tkinter as tk
from tkinter import *
from tkinter import simpledialog
import datetime
import requests

API_KEY = 'dc223d0162eed54cacd81a581a219b44'  # Our API key
API_SECRET = '588fcc02dfb549a295139437e4b78477' # Our API secrets

def fetch_top_tracks(username): # This gets our top tracks from the API
    url = f"http://ws.audioscrobbler.com/2.0/?method=user.getTopTracks&user={username}&api_key={API_KEY}&format=json&period=7day&limit=5"
    response = requests.get(url).json()

    if 'toptracks' not in response or len(response['toptracks']['track']) == 0:
        return None

    tracks = response['toptracks']['track']
    top_songs = [(track['name'], track['artist']['name']) for track in tracks]
    return top_songs
def display_top_tracks(username): #This displays our top tracks
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
date = datetime.date.today() # Gets the date
realDate = date.strftime("%B, %d, %Y") # Formats date to Month, Day, Year
def display_top_tracks_by_year(username, startDate, endDate):
    url = f"http://ws.audioscrobbler.com/2.0/?method=user.getweeklytrackchart&user={username}&api_key={API_KEY}&format=json"

## Prompt the user to enter their username
username = input("Enter your Lastfm username: ")
## Welcome message / Prompt user to enter a year
print(f"Hey, {username}! Today is {realDate}.")
selectedYear = input("Enter a year: (2021 - present): ")
if selectedYear == "2024":
    display_top_tracks(username)
elif selectedYear == "2023":
    ## Code to display top tracks from year 2023
