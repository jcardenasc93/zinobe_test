""" Get regions from https://rapidapi.com/apilayernet/api/rest-countries-v1 """

import os
import json
import requests

# Response handler
from utils.request_handler import RequestHandler


def get_regions():
    """ This method send request to the provided API
    to get all regions
    """
    url = os.getenv("REGIONS_URL")
    regions = None

    try:
        headers = {
            "x-rapidapi-key": os.environ["API_KEY"],
            "x-rapidapi-host": os.environ["API_HOST"]
        }
    except KeyError:
        print("Missing required environment variables")
    else:
        response = RequestHandler(url, headers).return_response()
        if response:
            # Extracts regions from retrieved info
            regions = list(
                set([country["region"] for country in response
                    ]))
            return regions
