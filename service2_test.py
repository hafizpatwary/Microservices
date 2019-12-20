import random, json

with open('countries.json') as file:
    data = json.loads(file.read())

countries = list(data.items())
quiz = random.sample(countries, 4)

package = dict()

for country in quiz:
	package.update({f"{country[0]}":f"{country[1]}"})

print(json.dumps(package))

