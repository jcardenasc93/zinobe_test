# Zinobe Challenge
This project contains the development of the techincal test for Python developer position at Zinobe

## Setup

### Requirements

* [python 3.8](https://www.python.org/downloads/release/python-388/)
* [pipenv](https://pipenv.pypa.io/en/latest/) (To install it just run `pip3 install pipenv`)
* [SQLite](https://sqlite.org/index.html)

### Steps to launch the project

Once all requirements installed in your system follow the next steps:

1. Clone the repo
2. Navigate to the project directory `cd zinobe_test `
3. Install the project requirements with `pipenv install`
4. Copy `.env.example` file to `.env` and adjust the environment variables values with the given in the file
5. Activate virtual environment with `pipenv shell`
6. Run the `main.py` script with `python main.py`

### Unit tests

Run unit test with the command `python -m unittest discover tests`

## Application Components

### main.py

This is the entry point of the app

### Services

Here you can found all the services layers required to handle different processes that are invoked in the main file

#### <a name='get_regions'></a>get_regions

This service implements the layer to module the request to the [first API](https://rapidapi.com/apilayernet/api/rest-countries-v1) in order to retrieve all the regions from that source

#### <a name='get_countries'></a>get_countries

Same as the previous layer, this module send a request to a [second API](https://restcountries.eu/) to retrieve information related to the first country coincidence that belongs to each one of the regions get previously

#### data_analysis

This module implements the [pandas](https://pandas.pydata.org/) tool to manipulate the retrieved data as a pandas data frame, this allows to easily calculate the total sum, average, min and max times that took the app retrieve each country info

#### reports

Finally this module contains the required layers to create and insert rows to the SQLite database and to generate `data.json` file with the countries info

### Utils

Here exists a unique module that is transversal for the [get_regions](#get_regions) and [get_countries](#get_countries). This module handles the sending requests process

