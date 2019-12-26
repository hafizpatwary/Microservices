from application import app
from application.functions import get_prize

@app.route('/', methods=["GET", "POST"])
def prize():

    country_service = 'http://countries:5000/'
    temperature_service = 'http://temperature:5000/'
    post = get_prize(country_service, temperature_service)

    return post












