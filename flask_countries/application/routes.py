from application import app
from application.functions import get_countries

@app.route('/', methods=['GET'])
def countries():

    no_of_countries = 5
    post = get_countries('./application/countries.json', no_of_countries)

    return post

