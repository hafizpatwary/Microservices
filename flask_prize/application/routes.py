from application import app
import requests, json, random


def get_prize(country_service, temperature_service):
    try:
        countries_response = requests.get(country_service)
        temperature_response = requests.get(temperature_service)

        if countries_response.status_code == 200 and temperature_response.status_code == 200:
            countries = countries_response.json()
            temperature = temperature_response.json()

            n_countries = len(countries["options"])
            temp = float(temperature["temperature"])

            prize_factor = abs(temp//(n_countries + 1))
            prize = (prize_factor * 10 + 10) if prize_factor < 5 else 90.00

            data = {
                "prize":prize,
                "city":f"{temperature['city']}"
            }

            return json.dumps(data, indent=2)

        else:
            exception = f"""Countries service response: {countries_response.status_code}
            \nTemperature service response: {temperature_response.status_code}"""
            raise Exception(exception)

    except Exception as err:
        print(f'An error occurred: {err}')


@app.route('/', methods=["GET", "POST"])
def prize():

    country_service = 'http://countries:5000/'
    temperature_service = 'http://temperature:5000/'
    post = get_prize(country_service, temperature_service)

    return post












