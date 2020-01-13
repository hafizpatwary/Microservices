from application import app
import random, json



def get_countries(jsonfile, number):
    """ Choose the file from which the function can select
    a set of random countries. The function returns a JSON
    object with the name and code of the country """

    try:
        with open(jsonfile) as file:
            data = json.load(file)

        country_list = list(data.items())
        countries = random.sample(country_list, number)

        json_countries = []
        for country in countries:
            json_countries.append(
                {
                "code":f"{country[0]}",
                "name":f"{country[1]}"
                })

        flags = json_countries
        flag = random.choice(flags)["code"]

        package = {
            "options":json_countries,
            "image":flag
        }

    except TypeError as error:
        raise Exception("Ensure JSON file is in correct format and number is an int type")


    return json.dumps(package, indent=2)


@app.route('/', methods=['GET'])
def countries():

    no_of_countries = 2
    post = get_countries('./application/countries.json', no_of_countries)

    return post

