import requests, random, json

with open('countries.json') as file:
    data = json.loads(file.read())

countries = list(data.items())
quiz = random.sample(countries, 4)

package2 = dict()

for country in quiz:
	package2.update({f"{country[0]}":f"{country[1]}"})

service2 = json.dumps(package2)



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

package3 = {"temperature":f"{temperature}"}

service3 = json.dumps(package3)
print(json.dumps(package3))
print(json.dumps(package2))

print(len(json.loads(service2)))


