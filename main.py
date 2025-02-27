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
import yaml

def getApi():
    try:
        f = open('./api.yaml', 'r')
        api = yaml.safe_load(f)
        f.close()
        return api
    except Exception as err:
        print(err)

def checkIpReputation(ip, api):
    headers = {
        'Accept': 'application/json',
        'Key': api['key']
    }

    try:
        resp = requests.get(api['url'], headers=headers, params={'ipAddress': ip})
    except requests.exceptions.RequestException as err:
        print(f"An exception occurred!\n{err}")

    data = resp.json()
    
    if 'data' in data:
        print(f"{data['data']['ipAddress']} was reported {data['data']['totalReports']} times. Confidence of Abuse is {data['data']['abuseConfidenceScore']}%")
    else:
        print(f"An exception occurred!\n{data}")

parser = argparse.ArgumentParser()

parser.add_argument('-ip', type=str, required=True, help='One IP or list of IPs')

args = parser.parse_args()

try:
    ips = open(args.ip, 'r')
except Exception as err:
    print(err)

for ip in ips:
    for apis in getApi()['data']:
        for api in apis.keys():
            print(api)
            #checkIpReputation(ip, api)
ips.close()
    
