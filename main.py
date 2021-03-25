""" Main project module """
from services.get_regions import get_regions
from services.get_countries import Countries
from services.data_analysis import DataAnalysis
from services.reports import DBManager

__author__ = "Juan Camilo Cardenas"
__version__ = "0.1.0"


def main():
    """ Entry point """
    regions = get_regions()
    if regions:
        countries = Countries.get_countries(regions)
        countries_data = DataAnalysis(countries)
        countries_data.time_statistics()
        app_db = DBManager()
        app_db.insert_row(countries_data.report)
    else:
        print("Cannot retrieve regions")


if __name__ == "__main__":
    main()
