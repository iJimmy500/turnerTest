import time
import webbrowser
import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk
import datetime
import requests
from datetime import date, timedelta
from colorama import Fore, Style, init
init()

username = input("Enter your Last.fm username: ")
def fetch_from_past(username):
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
    
   

fetch_from_past(username)
print("Thanks for using Tunie!")