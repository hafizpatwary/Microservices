import unittest, json, pytest, requests
from unittest import mock
from application import app, functions
from flask_testing import TestCase
from flask import url_for


class TestBase(TestCase):

    def create_app(self):
        # pass in test configurations
        config_name = 'testing'

        return app


def mocked_requests_get(*args, **kwargs):

    class MockResponse:

        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'http://countries:5000/':
    	countries_json = {
    	"options": [
    	{
    	"code": "ZA",
    	"name": "South Africa"
    	},
    	{
    	"code": "TG",
    	"name": "Togo"
    	},
    	{
    	"code": "YE",
    	"name": "Yemen"
    	},
    	{
    	"code": "NL",
    	"name": "Netherlands"
    	}
    	],
    	"image": "YE"
    	}

    	return MockResponse(countries_json, 200)

    elif args[0] == 'http://temperature:5000/':
    	return MockResponse({"temperature": "5.2"}, 200)

    return MockResponse(None, 404)


class TestServiceFunction(TestBase):

	# To patch 'requests.get' with our own method. The mock object is passed in to our test case method.
	@mock.patch('requests.get', side_effect=mocked_requests_get)
	def test_get_prize(self, mock_get):
		country_service = 'http://countries:5000/'
		temperature_service = 'http://temperature:5000/'

		prize_json = functions.get_prize(country_service, temperature_service)
		prize = json.loads(prize_json)
		prize_money = float(prize["prize"])

		self.assertTrue(prize_money >= 0)

	def test_get_countries_exception(self):
		
		with pytest.raises(Exception):
			assert functions.get_prize('http://countries:5000/', 'http://temperature:5000/')


class TestServiceRoutes(TestBase):

	@mock.patch('requests.get', side_effect=mocked_requests_get)
	def test_api(self, mock_get):
		response = self.client.get(url_for('prize'))
		self.assertEqual(response.status_code, 200)







