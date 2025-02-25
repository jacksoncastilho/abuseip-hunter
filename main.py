#! /usr/bin/python

# - [x] pint message
# - [x] read file
# - [x] handle exceptions with try/catch
# - [ ] handle end credits
# - [ ] algumens
# - [ ] add classes
# - [ ] documentation

import requests
import argparse
import sys

URL = 'https://api.abuseipdb.com/api/v2/check'
API_KEY = '351cb53585f43f957aab7acc5ad77afe8331d0a14ca2e2e0b53fe405c7183a186b3ddd379750d0fc'

parser = argparse.ArgumentParser()

parser.add_argument('-l', '--list', type=str, required=True, help='IP list')

args = parser.parse_args()

headers = {
    'Accept': 'application/json',
    'Key': API_KEY
}
try:
    f = open(args.list, "r")
    for ip in f:
        try:
            res = requests.get(URL, headers=headers, params={'ipAddress': ip})    
            data = res.json()
            if 'data' in data:
                print(f"{data['data']['ipAddress']} was reported {data['data']['totalReports']} times. Confidence of Abuse is {data['data']['abuseConfidenceScore']}%")
            else:
                print(f"An exception occurred!\n{data}")
                break
        except Exception as err:
            print(f"An exception occurred!\n{err}")
            break
except Exception as err:
    print(f"An exception occurred!\n{err}")
#finally:
#    f.close()

