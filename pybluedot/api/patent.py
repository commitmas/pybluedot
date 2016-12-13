import config
import requests
import json


class Patent(object):

    def __init__(self, query, api_key = config.API_KEY, concept_tags = False,
                 limit = None):
        self.query = query
        self.api_key = api_key
        self.concept_tags = concept_tags
        self.limit = limit


    def get(self):
        self.patent_params = { 'query' : self.query,
                               'api_key' : self.api_key,
                               'concept_tags' : self.concept_tags,
                               'limit' : self.limit }

        response = requests.get(config.PATENT_URL, params = self.patent_params)

        try:
            response.raise_for_status()

        except requests.exceptions.HTTPError as e:
            return "Error: " + str(e)

        body = response.json()

        if 'error' in body:
            raise Exception(body['error'])
        return body
# Current default is to return out json, need to add ability for file output
# which might be handled by here.
