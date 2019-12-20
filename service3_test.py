import requests, random, json

########################## remove api when uploading on github
api_key = 

cities = {"Manchester":"2643123",
"London":"2643741",
"Milan":"3172184",
"Paris":"2988507",
"Dhaka":"1185241",
"Singapore":"1880252",
"Oslo":"3143244"}


random_city = random.choice(list(cities))

city = cities[f"{random_city}"]

weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?id={city}&appid={api_key}").json()

temperature = float(weather['main']['temp']) - 273.15 # Transforming temperature in degree *C

package = {"temperature":f"{temperature}"}


print(json.dumps(package))