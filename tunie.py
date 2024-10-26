import time
import webbrowser
import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk
import datetime
import requests
from datetime import date, timedelta


API_KEY = 'dc223d0162eed54cacd81a581a219b44'
API_SECRET = '588fcc02dfb549a295139437e4b78477'

today_date = datetime.date.today()  
realDate = today_date.strftime("%B %d")  
current_date = datetime.date.today()

print(f"Find out what you played on {realDate} in the past!")
username = input("Enter your Last.fm username: ")

print(f"Hey {username}, check out your top tunes!")
print(f"Give me a few seconds to fetch your top tracks...")
time.sleep(1)

def fetch_from_past(username):
    one_year_ago = current_date - timedelta(days=365)
    from_timestamp = int(one_year_ago.strftime("%s")) 
    to_timestamp = from_timestamp + (7 * 24 * 60 * 60)
    
    url = (
        f"http://ws.audioscrobbler.com/2.0/?method=user.getRecentTracks"
        f"&user={username}&api_key={API_KEY}&format=json"
        f"&from={from_timestamp}&to={to_timestamp}&limit=5"
    )
    response = requests.get(url).json()
    
    
    if "recenttracks" in response:
        tracks = response["recenttracks"]["track"]
        for track in tracks:
            song_name = track["name"]
            artist_name = track["artist"]["#text"]
            track_url = track["url"]
            time_played = int(track["date"]["uts"])
            # timestamp = datetime.datetime.fromtimestamp(time_played).strftime('%Y-%m-%d %H:%M:%S')
            timestamp = datetime.datetime.fromtimestamp(time_played).strftime('%m/%d/%Y %H:%M')
            print(f"{artist_name} - {song_name}  | Played on: {timestamp}")
                  
    else:
        print("No tracks found.")
        
    time.sleep(0.5)
    
    
    return song_name if tracks else None, artist_name if tracks else None, track_url if tracks else None

fetch_from_past(username)
print("Thanks for using Tunie!")
