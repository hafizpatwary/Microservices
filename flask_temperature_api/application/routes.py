from application import app
from os import getenv
import requests, random, json


def get_temerature(cities, api_key):

    random_city = random.choice(list(cities))
    city_id = cities[random_city]
    weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}").json()
    temperature = float(weather['main']['temp']) - 273.15 # Transforming temperature in degree *C

    package = {"temperature":f"{temperature}"}

    return json.dumps(package, indent=2)


@app.route('/', methods=['GET'])
def temperature():
    api_key = getenv('API_KEY')
    cities = {"Manchester":"2643123",
              "London":"2643741",
              "Milan":"3172184",
              "Paris":"2988507",
              "Dhaka":"1185241",
              "Singapore":"1880252",
              "Oslo":"3143244"}

    post = get_temerature(cities, api_key)
    return post

