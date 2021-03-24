""" Module to handle modules responses """

import json
import requests


class RequestHandler:
    """ This class is used to get standard requests responses """

    def __init__(self, url: str, headers=None):
        """ ResponseHandler constructor """
        self.url = url
        self.headers = headers

    def return_response(self):
        """ Uses url and headers to send the requests and
        returns the response as python dict

        Returns:
            response (dict): The HTTP reponse as python dict
        """
        error = None
        data = None

        try:
            response = requests.get(self.url, headers=self.headers)
            if response.status_code == 200:
                data = json.loads(response.text)
        except ConnectionError:
            print("Cannot connect to the API")
        except TimeoutError:
            print("Timeout reached")
        finally:
            return data
