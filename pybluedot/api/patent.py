# Copyright 2016 Jeorry Balasabas
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pybluedot import config
import requests
from requests.exceptions import HTTPError


class Patent(object):
    """A API to search NASA's patent repository.

    Args:
        query (str, required): Search text to filter results.
        api_key (str, required): api.nasa.gov key for expanded usage.
            Default is DEMO_KEY in config.py.
        concept_tags (str, optional): Return an ordered dict of concepts from
            the patent abstract. Default is False.
        limit (int, optional): Number of patents to return. Default is None.
    """
    def __init__(self, query, api_key=config.API_KEY, concept_tags=False,
                 limit=None):
        self.query = query
        self.api_key = api_key
        self.concept_tags = concept_tags
        self.limit = limit

    def get(self):
        """Builds parameter dict that requests library
           will use for url query.
        """
        self.patent_params = {'query': self.query,
                              'api_key': self.api_key,
                              'concept_tags': self.concept_tags,
                              'limit': self.limit}

        response = requests.get(config.PATENT_URL, params=self.patent_params)

        try:
            response.raise_for_status()

        except HTTPError as e:
            raise HTTPError(str(e))

        body = response.json()

        if 'error' in body:
            raise Exception(body['error'])
        return body
