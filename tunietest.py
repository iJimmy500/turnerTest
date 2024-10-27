import time
import webbrowser
import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import scrolledtext  # Import for a scrollable text widget
from PIL import Image, ImageTk
import datetime
import requests
from datetime import date, timedelta
from colorama import Fore, Style, init

init()

API_KEY = 'dc223d0162eed54cacd81a581a219b44'
API_SECRET = '588fcc02dfb549a295139437e4b78477'

today_date = datetime.date.today()
realDate = today_date.strftime("%B %d")
current_date = datetime.date.today()


def show_popup(title, message):
    """Displays a popup window with the given title and message."""
    popup = tk.Tk()
    popup.title(title)
    popup.geometry("400x300")

    # Create a scrollable text widget
    text_area = scrolledtext.ScrolledText(popup, wrap=tk.WORD)
    text_area.pack(expand=True, fill='both')

    text_area.insert(tk.END, message)  # Insert the message into the text area
    text_area.config(state=tk.DISABLED)  # Disable editing
    button = tk.Button(popup, text="Close", command=popup.destroy)
    button.pack()

    popup.mainloop()  # Start the Tkinter event loop


def getTrackInfo(response):
    if "recenttracks" in response:
        tracks = response["recenttracks"]["track"]
        message = ""  # To collect all the track info for the popup
        for track in tracks:
            song_name = track["name"]
            artist_name = track["artist"]["#text"]
            track_url = track["url"]
            time_played = int(track["date"]["uts"])

            timestamp = datetime.datetime.fromtimestamp(time_played).strftime('%m/%d/%Y %H:%M')
            message += f"{artist_name} - {song_name}  | Played on: {timestamp}\n"

        if message:  # If we have track info, show it in a popup
            show_popup("Track Information", message)
        else:
            show_popup("Track Information", "No tracks found.")
    else:
        show_popup("Track Information", "No tracks found.")

    time.sleep(0.5)


def fetch_from_past_2023(username):
    target_date = current_date - timedelta(days=366)
    from_timestamp = int(datetime.datetime(target_date.year, target_date.month, target_date.day).timestamp())
    to_timestamp = from_timestamp + (24 * 60 * 60)

    url = (
        f"http://ws.audioscrobbler.com/2.0/?method=user.getRecentTracks"
        f"&user={username}&api_key={API_KEY}&format=json"
        f"&from={from_timestamp}&to={to_timestamp}&limit=5"
    )
    response = requests.get(url).json()
    getTrackInfo(response)


def fetch_from_past_2022(username):
    target_date = current_date - timedelta(days=366 + 365)
    from_timestamp = int(datetime.datetime(target_date.year, target_date.month, target_date.day).timestamp())
    to_timestamp = from_timestamp + (24 * 60 * 60)

    url = (
        f"http://ws.audioscrobbler.com/2.0/?method=user.getRecentTracks"
        f"&user={username}&api_key={API_KEY}&format=json"
        f"&from={from_timestamp}&to={to_timestamp}&limit=5"
    )
    response = requests.get(url).json()
    getTrackInfo(response)


def fetch_from_past_2021(username):
    target_date = current_date - timedelta(days=366 + 365 + 365)
    from_timestamp = int(datetime.datetime(target_date.year, target_date.month, target_date.day).timestamp())
    to_timestamp = from_timestamp + (24 * 60 * 60)

    url = (
        f"http://ws.audioscrobbler.com/2.0/?method=user.getRecentTracks"
        f"&user={username}&api_key={API_KEY}&format=json"
        f"&from={from_timestamp}&to={to_timestamp}&limit=5"
    )
    response = requests.get(url).json()
    getTrackInfo(response)


def fetch_top_tracks(username):  # This gets our top tracks from the API
    url = f"http://ws.audioscrobbler.com/2.0/?method=user.getTopTracks&user={username}&api_key={API_KEY}&format=json&period=7day&limit=5"
    response = requests.get(url).json()

    if 'toptracks' not in response or len(response['toptracks']['track']) == 0:
        return None

    tracks = response['toptracks']['track']
    top_songs = [(track['name'], track['artist']['name']) for track in tracks]
    return top_songs


def display_top_tracks(username):  # This displays our top tracks
    try:
        top_songs = fetch_top_tracks(username)
        if top_songs is None:
            show_popup("Top Tracks", f"No top tracks found for {username} this week.")
        else:
            message = f"Top 5 Tracks for {username} (Past 7 Days):\n"
            for i, (song, artist) in enumerate(top_songs, 1):
                message += f"{i}. '{song}' by {artist}\n"
            show_popup("Top Tracks", message)
    except Exception as e:
        show_popup("Error", f"Error: {str(e)}")


print(f"Find out what you played on {Fore.CYAN} {realDate} {Style.RESET_ALL} in the past!")
username = input("Enter your Last.fm username: ")

while True:
    selectedYear = input(f"{Fore.CYAN} Enter a year starting from 2021 {Fore.RED}(Enter \"Done\" to exit): ")
    if selectedYear == "Done":
        print("Thanks for using Tunie!")
        break

    print(f"{Fore.GREEN}Give me a few seconds to fetch your top tracks...{Style.RESET_ALL}")

    if selectedYear == "2024":
        display_top_tracks(username)
    elif selectedYear == "2023":
        fetch_from_past_2023(username)
    elif selectedYear == "2022":
        fetch_from_past_2022(username)
    elif selectedYear == "2021":
        fetch_from_past_2021(username)

time.sleep(1)
print(f"{Fore.GREEN}Thanks for using Tunie!")
