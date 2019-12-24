from application import app
from application.functions import get_prize

@app.route('/', methods=["GET", "POST"])
def prize():

    country_service = 'http://localhost:5001/'
    temperature_service = 'http://localhost:5002/'
    post = get_prize(country_service, temperature_service)

    return post












