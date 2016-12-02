import requests

patent_url = 'https://api.nasa.gov/patents/content'

#api key obtained from NASA
my_api_key = 'aApglMV0QO74TpuZACRnSUvGel8ayxf7Z067Nnsa'
query = 'plastic'
limit = '10'
con_tags = False

#NASA Patents query parameters
get_params = {'query': query, 'limit': limit, 'api_key': my_api_key}

getRequest = requests.get(patent_url, params = get_params)

print getRequest.json()
