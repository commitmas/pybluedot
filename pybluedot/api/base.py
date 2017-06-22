import pybdotconfig
import configparser
import requests

class NasaApiException(Exception):
    """Raised for any exception caused by a call to the Nasa API"""

class Pybdotapi(object):
    """Default base class, all api classes will inherit from this"""
    def __init__(self, url=None, payload=None):
        self.url = url
        self.payload = payload

    def get_api_key(self):
        config = configparser.ConfigParser()
        config.read('pybluedotconf.py')
        api_key = config['Global']['api_key']
        return api_key

    def api_get(self, url=self.url, payload=self.payload):
        config = configparser.ConfigParser()
        payload['api_key'] = get_api_key()
        response = requests.get(url, params=payload)
        response.raise_for_status()
        body = response.json()

        if 'error' in body:
            raise NasaApiException(body['error'])

        return body


    


