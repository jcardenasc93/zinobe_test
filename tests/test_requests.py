""" Unit testing """
from unittest import main
from unittest import TestCase
from unittest.mock import patch
import requests
import json
import hashlib

from services.get_regions import get_regions
from services.get_countries import Countries
from utils.request_handler import RequestHandler

FAKE_URL = "https://fake.com"


class MockResponse:
    """ This class mocks the response object created from requests package """

    def __init__(self, status_code):
        self.status_code = status_code
        self.text = json.dumps({"msg": "Success"})


class TestRequestHandler(TestCase):
    """ Set of test cases for request handler """

    @patch.object(requests, "get")
    def test_success_response(self, mock_request_response):
        """Test success request response"""
        mock_request_response.return_value = MockResponse(200)
        response = RequestHandler(FAKE_URL).return_response()
        self.assertEqual("Success", response.get("msg"))

    @patch.object(requests, "get")
    def test_fail_response(self, mock_request_response):
        """Test success request response"""
        mock_request_response.return_value = MockResponse(400)
        response = RequestHandler(FAKE_URL).return_response()
        self.assertEqual(None, response)


class TestGetRegions(TestCase):
    """ Tests set for get regions """

    def setUp(self):
        self.mock_response = [{
            "region": "Asia"
        }, {
            "region": "Asia"
        }, {
            "region": "America"
        }]

    @patch.object(RequestHandler, "return_response")
    def test_retrieve_regions(self, mock_request_handler):
        """ Test regions list """
        mock_request_handler.return_value = self.mock_response
        regions = get_regions()
        self.assertEqual(2, len(regions))


class TestGetCountries(TestCase):
    """ Tests set for get countries """

    def setUp(self):
        self.mock_response = [{
            "region": "Asia",
            "name": "Japan",
            "languages": [{
                "name": "Japanese"
            }]
        }, {
            "region": "Asia",
            "name": "Kuwait",
            "languages": [{
                "name": "Arabic"
            }]
        }]

    @patch.object(RequestHandler, "return_response")
    def test_retrieve_regions(self, mock_request_handler):
        """ Test countries list """
        mock_request_handler.return_value = self.mock_response
        countries = Countries.get_countries(["Asia"])
        self.assertEqual(1, len(countries))
        self.assertEqual(
            hashlib.sha1(b"Japanese").hexdigest(), countries[0].get("Language"))


if __name__ == '__main__':
    main()
