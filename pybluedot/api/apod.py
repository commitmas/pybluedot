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
