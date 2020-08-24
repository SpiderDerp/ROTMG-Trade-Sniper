import requests
import json
from playsound import playsound

player = input("Input Player Name: ")

url = "https://nightfirec.at/realmeye-api/?player=" + player + "&filter=player_last_seen"

response = requests.get(url)

data = response.text

parsed = json.loads(data)

previous_parsed = parsed

while(True):
    url = "https://nightfirec.at/realmeye-api/?player=" + player + "&filter=player_last_seen"

    response = requests.get(url)

    data = response.text

    parsed = json.loads(data)

    if(previous_parsed != parsed):
        print("There has been a change in player status")
        playsound('C:\\Users\\sfsre\\Documents\\ROTMG Trade Sniper\\crabrave.mp3') #change to whatever directory crab rave is in
        break

    previous_parsed = parsed




# Made by SpiderDerp - 2020