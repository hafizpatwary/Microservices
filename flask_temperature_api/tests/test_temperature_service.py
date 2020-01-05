import unittest, json, pytest
from application import app, functions
from flask_testing import TestCase
from os import getenv
from flask import url_for

class TestBase(TestCase):

    def create_app(self):
        # pass in test configurations
        config_name = 'testing'

        return app


class TestServiceFunction(TestBase):

    def test_get_temerature(self):

        cities = {"Manchester":"2643123", "London":"2643741"}

        temperature_json = functions.get_temerature(cities, getenv('API_KEY'))
        temperature = json.loads(temperature_json)
        temperature_degree = float(temperature["temperature"])

        self.assertTrue(-273 <= temperature_degree <= 100)


class TestServiceRoutes(TestBase):

    def test_api_call(self):

        response = self.client.get(url_for('temperature'))

        self.assertEqual(response.status_code, 200)
