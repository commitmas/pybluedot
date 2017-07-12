from . import base
from pprint import pprint

class Patent(object):
    """A API to search NASA's patent repository.

    Args:
        query (str, required): Search text to filter results.
        api_key (str, required): api.nasa.gov key for expanded usage.
        concept_tags (str, optional): Return an ordered dict of concepts from
            the patent abstract. Default is False.
        limit (int, optional): Number of patents to return. Default is None.
    """

    def __init__(self, query, concept_tags=None, limit=None):
        self.query = query
        self.concept_tags = concept_tags
        self.limit = limit
        self.url = base.get_url('PATENT')

    def get(self):
        self.payload = {
            'query' : self.query,
            'concept_tags' : self.concept_tags,
            'limit' : self.limit,
        }
        self.response = base.api_get(self.url, self.payload)
        return self.response

    def __repr__(self):
        return pprint(self.response)


