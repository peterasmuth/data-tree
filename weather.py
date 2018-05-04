from json import JSONDecodeError

import requests
import csv
from datetime import datetime

def get_weather():

    '''Pull the JSON file using the wundergound API'''
    print("Requesting data..")
    weather_data = ""
    while True:
        try:
            weather_data = requests.get("http://api.wunderground.com/api/ec4e28e53161c067/conditions/q/MT/Bozeman.json").json()
            break
        except JSONDecodeError:
            print("Retrying request...")
            continue
        break



    '''Pull out desired values'''
    city = weather_data["current_observation"]["display_location"]["city"]
    station = weather_data["current_observation"]["station_id"]
    description = weather_data["current_observation"]["weather"]
    temp_f = weather_data["current_observation"]["temp_f"]
    humidity = weather_data["current_observation"]["relative_humidity"]
    wind = weather_data["current_observation"]["wind_mph"]
    wind_gust = weather_data["current_observation"]["wind_gust_mph"]
    wind_dir = weather_data["current_observation"]["wind_dir"]
    precip_last_hour = weather_data["current_observation"]["precip_1hr_in"]

    '''Put them in a list'''
    new_data = [datetime.now(), city, station, description, temp_f, humidity, wind, wind_dir, wind_gust, precip_last_hour]

    '''Writes the new row to a csv'''
    with open('weather.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(new_data)


get_weather()