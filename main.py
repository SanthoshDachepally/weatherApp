# WEATHER REPORT PROJECT
import requests
import os
import json
import pyttsx3

while True:
    city = input("Enter the name of the city or q to exit\n").lower()
    if city == "q":
        break
    try:
        url = f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"
        r = requests.get(url)
        wdic = json.loads(r.text)
        temp = wdic["current"]["temp_c"]
        print(f"The current weather in {city} is {temp} degrees celsius.")
        pyttsx3.speak(f"The current weather in {city} is {temp} degrees celsius.")
    except Exception as e:
        print(f"Please type correct name")
