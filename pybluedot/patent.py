import config

import requests
import json


class Patent(object):
#patent_params is a dictionary of arguments created from commands.py
    def get(self, patent_params):

    response = requests.get(config.patent_url, params = patent_params)

    if response.status_code == 429:
        raise Exception('You have exceeded your rate limit')

    body = response.json()

    if 'error' in body:
        raise Exception(body['error'])
    return body
# Current default is to return out json, need to add ability for file output
# which might be handled by here.
