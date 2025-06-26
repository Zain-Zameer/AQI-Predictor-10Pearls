import requests
import json
import csv
import os

API_KEY = "d0880b1c-e430-4eba-8bcb-68c6605e7a6e"
city = "Islamabad"
state = "Islamabad"
country = "Pakistan"

url = f"https://api.airvisual.com/v2/city?city={city}&state={state}&country={country}&key={API_KEY}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    if data["status"] != "success":
        print("API returned failure status.")
        exit()

    pollution = data["data"]["current"]["pollution"]
    weather = data["data"]["current"]["weather"]
    location = data["data"]["location"]

    row = {
        "timestamp": pollution["ts"],
        "city": data["data"]["city"],
        "state": data["data"]["state"],
        "country": data["data"]["country"],
        "latitude": location["coordinates"][1],
        "longitude": location["coordinates"][0],
        "aqius": pollution["aqius"],
        "mainus": pollution["mainus"],
        "aqicn": pollution["aqicn"],
        "maincn": pollution["maincn"],
        "temperature": weather["tp"],
        "humidity": weather["hu"],
        "pressure": weather["pr"],
        "wind_direction": weather["wd"],
        "wind_speed": weather["ws"]
    }
    print(row)
    
    with open("Data/weather_init.csv","a") as f:
        f.write("\n")
        for key in row:
            if(key!="wind_speed"):
                f.write(f'{row[key]},')
            else:
                f.write(f'{row[key]}')
    print("written successfully")
    

else:
    print(f"❌ Error {response.status_code}: {response.text}")
