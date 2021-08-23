import os
import requests
import json

from colorbrains_research import research_datapath

import pandas as pd


API_HOST = os.getenv('API_HOST', 'http://localhost')


def research_filepath(filename):
    return os.path.join(research_datapath, filename)


def read_data(filename):
    if os.path.isfile(research_filepath(filename)):
        return pd.read_csv(research_filepath(filename), index_col=0)
    return None


def write_data(df, filename):
    df.to_csv(research_filepath(filename))


def get_apidata(endpoint, overwrite=False):
    filename = f'{endpoint}.csv'
    data = read_data(filename)
    if data is not None and not overwrite:
        return data
    
    resp = requests.get(f'{API_HOST}/{endpoint}')
    data = json.loads(resp.json())['data']
    df = pd.DataFrame(data)
    write_data(df, filename)
    return df


def get_basecolors(overwrite=False):
    return get_apidata('basecolors')

def get_categorized_colormaps(overwrite=False):
    return get_apidata('categorized_colormaps')

def get_colormaps(overwrite=False):
    return get_apidata('colormaps')

def get_namedcolors(overwrite=False):
    return get_apidata('namedcolors')
