""" Data anlysisis module with pandas """
import pandas as pd

class DataAnalysis:
    """ Class implementation for data analysis """
    def __init__(self, countries: list):
        self.countries_df = pd.DataFrame(countries)
        print(self.countries_df)
