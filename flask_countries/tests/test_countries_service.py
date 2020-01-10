import unittest, json, pytest
from application import app, routes
from flask_testing import TestCase
from flask import url_for

class TestBase(TestCase):

    def create_app(self):
        # pass in test configurations
        config_name = 'testing'

        return app


class TestServiceFunction(TestBase):

    def test_get_countries(self):

        countries_json = routes.get_countries('./application/countries.json', 4)
        countries = json.loads(countries_json)

        number_of_countries = len(countries["options"])

        self.assertEqual(number_of_countries, 4)

    def test_get_countries_exception(self):

        with pytest.raises(Exception):
            assert routes.get_countries('./countries.json', 4)


class TestServiceRoutes(TestBase):

    def test_api_call(self):

        response = self.client.get(url_for('countries'))

        self.assertEqual(response.status_code, 200)
