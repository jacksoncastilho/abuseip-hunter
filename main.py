#! /usr/bin/python

import requests
import json
import argparse

API_KEY = "api_key_here!"

parser = argparse.ArgumentParser()

parser.add_argument('-l', '--list', type=str, required=True, help='IP list')

args = parser.parse_args()

url = 'https://api.abuseipdb.com/api/v2/check'

querystring = {
    'ipAddress': '20.161.75.217'
}

headers = {
    'Accept': 'application/json',
    'Key': 'API_KEY'
}

response = requests.request(method='GET', url=url, headers=headers, params=querystring)

decodedResponse = json.loads(response.text)
print(json.dumps(decodedResponse, sort_keys=True, indent=4))
