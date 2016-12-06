import argparse
import requests
import json


def patent(**kwargs):
    patent_url = 'https://api.nasa.gov/patents/content'
    get_params = {}
    for key, value in kwargs.iteritems():
        get_params[key] = value
    get_response = requests.get(patent_url, params = kwargs)

    if get_response.status_code == 429:
        raise Exception('You have exceeded your rate limit')

    body = get_response.json()

    if 'error' in body:
        raise Exception(body['error'])
# Current default is to print out json, need to add ability for file output
    pretty_print = json.dumps(body, indent=2)
    return pretty_print


def main():
    ap = argparse.ArgumentParser(description = 'Search NASA patent portfolio')
    ap.add_argument('-a', '--api_key',
                    help = 'Your NASA API key', required=True)
    ap.add_argument('-q', '--query', help = 'Text to search on', required=True)
    ap.add_argument('-c', '--concept_tags',
                    help = 'Return ordered dict of concepts from the abstract')
    ap.add_argument('-l', '--limit', help = 'Number of patents to return',
                   type=int)
    args = ap.parse_args()

#need to add option to output json file
    print(patent(**vars(args)))

if __name__ == '__main__':
    main()
