from .. import pybdotconfig
import json
import requests

class NasaApiException(Exception):
    """Raised for any exception caused by a call to the Nasa API"""

def get_api_key():
    config = pybdotconfig.init_config()
    config.read('pybdot.ini')
    api_key = config['Global']['API_KEY']
    return api_key

def get_url(api):
    """Grabs URL from pybdot.ini for the corresponding API."""
    config = pybdotconfig.init_config()
    config.read('pybdot.ini')
    url = config[api]['url']
    return url

def api_get(url, payload):
    payload = dict((k, v) for k, v in payload.items() if v)
    payload['api_key'] = get_api_key()
    response = requests.get(url, params=payload)
    response.raise_for_status()
    body = response.json()

    if 'error' in body:
        raise NasaApiException(body['error'])

    return body


class Pybdot(object):
    """Default base class, all api classes will inherit from this"""

    def __init__(self, **kwargs):
        pass




    


