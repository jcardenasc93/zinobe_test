""" Get country from hhttps://restcountries.eu/rest/v2/region/<region:str> """

import os
import json
import requests
import hashlib
import time

# Response handler
from utils.request_handler import RequestHandler


class Countries:
    """ Class to process countries """

    @classmethod
    def get_countries(cls, regions: list):
        """ This method send request to the provided API
        to get first country from specific region
        """
        countries = []
        base_url = os.getenv("COUNTRIES_URL")
        for region in regions:
            if region:
                # Makes request
                url = base_url.format(region.lower())
                # Starts count time since get reponse from API
                start_time = time.time()
                response = RequestHandler(url).return_response()
                if response:
                    # Extracts info
                    country = response[0]
                    country_name = country.get("name")
                    language = country.get("languages")[0].get("name")
                    language = cls.encrypt_language(language)
                    country = {
                        "Region": region,
                        "Country Name": country_name,
                        "Language": language
                    }
                    country["Time"] = cls.calcs_elapsed_time(start_time)
                    countries.append(country)

        return countries

    @classmethod
    def encrypt_language(cls, language: str):
        """ Encrypts languages with SHA1 """
        encrypt = hashlib.sha1(bytes(language, 'utf-8'))
        return encrypt.hexdigest()

    @classmethod
    def calcs_elapsed_time(cls, start_time):
        return time.time() - start_time
