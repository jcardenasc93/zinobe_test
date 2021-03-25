""" Data anlysisis module with pandas """
import pandas as pd

class DataAnalysis:
    """ Class implementation for data analysis """
    def __init__(self, countries: list):
        self.countries_df = pd.DataFrame(countries)
        print(self.countries_df)

    def time_statistics(self):
        """ This method calcs the total sum of the values in the df column Time,
        its average, the minimum and maximum
        """
        TIME_KEY = 'Time'
        self.total_time = self.countries_df[TIME_KEY].sum()
        self.statistics_df = self.countries_df[TIME_KEY].describe()
        self._time_report()

    def _time_report(self):
        """ Generates the time statistics report """
        average = self.statistics_df['mean']
        min_time = self.statistics_df['min']
        max_time = self.statistics_df['max']

        print("{:<10} {:<15}".format("", "Time statistics"))
        print("{:<15} {:<15}".format('Total time', self.total_time))
        print("{:<15} {:<15}".format('Average time', average))
        print("{:<15} {:<15}".format('Min time', min_time))
        print("{:<15} {:<15}".format('Max time', max_time))

        self.report = [(self.total_time, average, max_time, min_time)]

