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

from datetime import date
from pybluedot import config
import requests
from requests.exceptions import HTTPError

class Apod(object):
    """A API to return NASA's astronomy picture of the day.

    Args:
        date (str, optional): The date of the APOD image to retrieve.
            format YYYY-MM-DD
            Default is today's date.
        dh (bool, optional): Retrieve url for for high res image.
        api_key (str, required): api.nasa.gov key for expanded usage.
            Default is DEMO_KEY in config.py.
    """

    def __init__(self, date=None, api_key=config.API_KEY, hd=False):
        self.date = date
        self.api_key = api_key
        self.hd = hd

    def get(self):
        """Builds parameter dict that requests library
           will use for url query.
        """
        self.patent_params = {'date': self.date,
                              'api_key': self.api_key,
                              'hd': self.hd}

        response = requests.get(config.APOD_URL, params=self.patent_params)

        try:
            response.raise_for_status()

        except HTTPError as e:
            raise HTTPError(str(e))

        body = response.json()

        if 'error' in body:
            raise ValueError(body['error'])
        return body
