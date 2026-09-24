import requests

def make_request(url, headers = None, params = None):
    response = requests.get(url, headers = headers, params = params)
    response.raise_for_status()
    return response.json()