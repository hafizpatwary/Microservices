from application import app
from application.functions import get_temerature
from os import getenv


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

