""" Main project module """
from services.get_regions import get_regions
from services.get_countries import Countries
from services.data_analysis import DataAnalysis

__author__ = "Juan Camilo Cardenas"
__version__ = "0.1.0"


def main():
    """ Entry point """
    regions = get_regions()
    if regions:
        countries = Countries.get_countries(regions)
        DataAnalysis(countries)
    else:
        print("Cannot retrieve regions")


if __name__ == "__main__":
    main()
