#! /usr/bin/python

# - [x] pint message
# - [x] read file
# - [ ] handle exceptions with try/catch
# - [ ] end credits
# - [ ] algumens
# - [ ] add classes
# - [ ] documentation

import requests
import argparse

URL = 'https://api.abuseipdb.com/api/v2/check'
API_KEY='api_key_here!'

parser = argparse.ArgumentParser()

parser.add_argument('-l', '--list', type=str, required=True, help='IP list')

args = parser.parse_args()

headers = {
    'Accept': 'application/json',
    'Key': API_KEY
}

f = open(args.list, "r")
for ip in f:
    querystring = {
        'ipAddress': ip
    }

    r = requests.get(URL, headers=headers, params=querystring).json()
    
    print(f"{r['data']['ipAddress']} was reported {r['data']['totalReports']} times. Confidence of Abuse is {r['data']['abuseConfidenceScore']}%")

f.close()

