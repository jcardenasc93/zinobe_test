""" Get country from hhttps://restcountries.eu/rest/v2/region/<region:str> """

import os
import json
import requests

# Response handler
from utils.request_handler import RequestHandler


def get_countries(regions: list):
    """ This method send request to the provided API
    to get first country from specific region
    """
    countries = []
    base_url = os.getenv("COUNTRIES_URL")
    for region in regions:
        if region:
            # Makes request
            url = base_url.format(region.lower())
            response = RequestHandler(url).return_response()
            if response:
                # Extracts info
                country = response[0]
                country_name = country.get("name")
                language = country.get("languages")[0].get("name")
                country = {"Region": region, "Country Name": country_name, "Language": language}
                countries.append(country)

    return countries
