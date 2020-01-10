import unittest
from flask import abort, url_for
from flask_testing import TestCase
import unittest, json, pytest, requests, os
from unittest import mock
from application import app, db
from application.models import Prize, Countries, Answers



class TestBase(TestCase):

    def create_app(self):
        # pass in test configurations
        config_name = 'testing'
        app.config.update(
            SQLALCHEMY_DATABASE_URI=f"mysql+pymysql://{os.getenv('MYSQL_USERNAME')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_IP')}/testdiet")
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        db.session.commit()
        db.drop_all()
        db.create_all()

        # create countries
        country_1 = Countries(country_id="AD", country="Andorra")
        country_2 = Countries(country_id="AE", country="United Arab Emirates")
        country_3 = Countries(country_id="AF", country="Afghanistan")

        # save users to database
        db.session.add(country_1)
        db.session.add(country_2)
        db.session.add(country_3)

        # commit all changes to database
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """
        db.session.remove()
        db.drop_all()


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
        "code": "AD",
        "name": "Andorra"
        },
        {
        "code": "AE",
        "name": "United Arab Emirates"
        },
        {
        "code": "AF",
        "name": "Afghanistan"
        },
        {
        "code": "NL",
        "name": "Netherlands"
        }
        ],
        "image": "AF"
        }

        return MockResponse(countries_json, 200)

    elif args[0] == 'http://temperature:5000/':
        return MockResponse({"temperature": "5.2"}, 200)

    elif args[0] == 'http://prize:5000':
        return MockResponse({"prize": 20.0}, 200)

    return MockResponse(None, 404)

class TestQuizRoute(TestBase):

    # To patch 'requests.get' with our own method. The mock object is passed in to our test case method.
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_quiz_route(self, mock_get):
        """ Test login required to create diet """

        target_url = url_for('quiz')
        response = self.client.get(target_url)

        self.assertEqual(response.status_code, 200)


class TestOutcomeRoute(TestBase):

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_outcome_get(self, mock_get):

        response = self.client.get(url_for('outcome'))

        self.assertEqual(response.status_code, 302)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_outcome_post(self, mock_get):
        post = self.client.post(url_for('outcome'), data={'answer':'AD', 'flag':'AD'})

        self.assertEqual(post.status_code, 200)


class TestRetrieveRoute(TestBase):

    def test_retrieve_get(self):
        response = self.client.get(url_for('retrieve'))

        # Assuring Method Not Allowed
        self.assertEqual(response.status_code, 405)

    def test_retrieve_post(self):
        response = self.client.post(url_for('retrieve'), data=dict(prize='10', email='h@gmail.com'))

        prizeData = Prize(
            email='h@gmail.com',
            prize='10'
            )
        db.session.add(prizeData)
        db.session.commit()

        prize = Prize.query.filter_by(id=1).first()

        self.assertTrue(prize.email, 'h@gmail.com')
        # Assuring response is correct
        self.assertEqual(response.status_code, 200)