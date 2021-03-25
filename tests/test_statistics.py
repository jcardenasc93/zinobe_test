""" Unit testing """
from unittest import main
from unittest import TestCase
from unittest.mock import patch
import json

from services.data_analysis import DataAnalysis


class TestDataAnalysis(TestCase):
    """ Tests set for get countries """

    def setUp(self):
        self.mock_countries = [{
            "Region": "Asia",
            "Country Name": "Japan",
            "Language": "04a422d38c95415cece1ac86e1ad2a1030048c03",
            "Time": 3
        }, {
            "Region": "Europe",
            "Country Name": "Germany",
            "Language": "af4f4762f9bd3f0f4a10caf5b6e63dc4ce543724",
            "Time": 1
        }]

    def test_retrieve_regions(self):
        """ Test time statistics """
        test_statistics = DataAnalysis(self.mock_countries)
        test_statistics.time_statistics()
        average = test_statistics.statistics_df['mean']
        min_time = test_statistics.statistics_df['min']
        max_time = test_statistics.statistics_df['max']

        self.assertEqual(4, test_statistics.total_time)
        self.assertEqual(2, average)
        self.assertEqual(1, min_time)
        self.assertEqual(3, max_time)


if __name__ == '__main__':
    main()
