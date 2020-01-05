import requests, random, json


def get_temerature(cities, api_key):

    random_city = random.choice(list(cities))
    city_id = cities[random_city]

    weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}").json()
    temperature = float(weather['main']['temp']) - 273.15 # Transforming temperature in degree *C

    package = {"temperature":f"{temperature}"}

    return json.dumps(package, indent=2)


