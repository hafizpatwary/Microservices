import json
import random

with open('countries.json') as f:
    data = json.loads(f.read())

countries = list(data.items())
answers = random.sample(countries, 5)



