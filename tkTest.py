import customtkinter
import tkinter
import time
import webbrowser
import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk
import datetime
import requests
from datetime import date, timedelta
from colorama import Fore, Style, init

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

API_KEY = 'dc223d0162eed54cacd81a581a219b44'
API_SECRET = '588fcc02dfb549a295139437e4b78477'

today_date = datetime.date.today()  
realDate = today_date.strftime("%B %d")  
current_date = datetime.date.today()

def yearPicker(choice):
    yearOption.configure(text=choice)
    
def yearPicker2():
    yearOption.configure(text=yearOption.get())
    
years = ['2021', '2022', '2023', '2024']

# fetch from 2021
def fetch_from_past_2021(username):
    target_date = current_date - timedelta(days=366+365+365)
    from_timestamp = int(datetime.datetime(target_date.year, target_date.month, target_date.day).timestamp())
    to_timestamp = from_timestamp + (24 * 60 * 60)

    url = (
        f"http://ws.audioscrobbler.com/2.0/?method=user.getRecentTracks"
        f"&user={username}&api_key={API_KEY}&format=json"
        f"&from={from_timestamp}&to={to_timestamp}&limit=5"
    )
    response = requests.get(url).json()
    getTrackInfo(response)
    print()
    
    # fetch from 2022
def fetch_from_past_2022(username):
    target_date = current_date - timedelta(days=366+365)
    from_timestamp = int(datetime.datetime(target_date.year, target_date.month, target_date.day).timestamp())
    to_timestamp = from_timestamp + (24 * 60 * 60)

    url = (
        f"http://ws.audioscrobbler.com/2.0/?method=user.getRecentTracks"
        f"&user={username}&api_key={API_KEY}&format=json"
        f"&from={from_timestamp}&to={to_timestamp}&limit=5"

    )
    response = requests.get(url).json()
    getTrackInfo(response)
    print()
    
# fetch 2023
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
    print()



# fetch from this year
def fetch_top_tracks(username): # This gets our top tracks from the API
    url = f"http://ws.audioscrobbler.com/2.0/?method=user.getTopTracks&user={username}&api_key={API_KEY}&format=json&period=7day&limit=5"
    response = requests.get(url).json()

    if 'toptracks' not in response or len(response['toptracks']['track']) == 0:
        return None

    tracks = response['toptracks']['track']
    top_songs = [(track['name'], track['artist']['name']) for track in tracks]
    return top_songs

    
    # get track info
def getTrackInfo(response):
    if "recenttracks" in response:
        tracks = response["recenttracks"]["track"]
        for track in tracks:
            song_name = track["name"]
            artist_name = track["artist"]["#text"]
            track_url = track["url"]
            time_played = int(track["date"]["uts"])

            timestamp = datetime.datetime.fromtimestamp(time_played).strftime('%m/%d/%Y %H:%M')
            print(f"{artist_name} - {song_name}  | Played on: {timestamp}")
            
    # easter eggs
def fetch_eastereggs(username):
    if username == 'Marty Mcfly': 
        print("Survival Tactics(feat. Capital Steez)")
    if username == 'Drake': 
        print("Millie Bobby Brown")
    if username == 'none': 
        print("I dont think thats a real username")
    if username == 'Pitbbull':
        print("Celebrate from Penguins of Madagascar")
    if username == 'Los':
        print("Every song from Challengers")
    if username == 'rowdyhacks':
        print("Howdy Howdy")
    if username == 'brainrot':
        print("Skibidi fanum tax")
    if username == 'kanye':
        print("Did you say kanye?")
    if username == 'Cj':
        print("The Theme from San Andreas by Michael Hunter")
    if username == 'Niko Bellic':
        print("Soviet Connection by Michael Hunter")
    if username == 'geeker':
        webbrowser.open("https://www.tiktok.com/t/ZP88sF3q4/")
    if username == 'coolin':
        webbrowser.open("https://www.instagram.com/p/DA6F_NFtaQX/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==")
    if username == 'gmail':
        webbrowser.open('https://www.instagram.com/reel/DBRSlv4xouI/?utm_source=ig_web_button_share_sheet&igsh=MzRlODBiNWFlZA==')
            
def fetch_based_on_year(selected_year):
    username = usersname.get()  
    if selected_year == "2021":
        fetch_from_past_2021(username)
        fetch_eastereggs(username)
    elif selected_year == "2022":
        fetch_from_past_2022(username)
        fetch_eastereggs(username)
    elif selected_year == "2023":
        fetch_from_past_2023(username) 
        fetch_eastereggs(username)
    elif selected_year == "2024":
        tracks = fetch_top_tracks(username)
        fetch_eastereggs(username)
        if tracks:
            for song, artist in tracks:
                print(f"{artist} - {song}")
        else:
            print("No top tracks found!")

root = customtkinter.CTk()
root.geometry("500x350")
root.title("Throwback")

def login():
    username = usersname.get()
    fetch_from_past_2021(username)

def two_commands():
    selected_year = yearOption.get()  # Read the selected year
    login()
    fetch_based_on_year(selected_year)  # Pass the selected year


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)

date_label = customtkinter.CTkLabel(master=frame, text=f"Today's date: {realDate}")
date_label.pack(pady=0.5, padx=5)

label = customtkinter.CTkLabel(master=frame, text="Throwback", font=("Helvetica", 24))
label.pack(pady=12, padx=10)

usersname = customtkinter.CTkEntry(master=frame, placeholder_text="Last.fm Username", corner_radius =10)
usersname.pack(pady=12, padx=10)

yearOption = customtkinter.CTkOptionMenu(master=frame, values=years)
yearOption.pack(pady=10, padx=10)

button = customtkinter.CTkButton(master=frame, text="Check top songs!", command=two_commands)
button.pack(pady=1, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Agree to staying locked in")
checkbox.pack(pady=12, padx=10)

credit = customtkinter.CTkLabel(master=frame, text_color = "lightcoral", text="Made @ RowdyhacksX by Throwback Team")
credit.pack(pady=12, padx=10)

root.mainloop()