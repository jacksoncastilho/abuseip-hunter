#! /usr/bin/python

# - [x] pint message
# - [ ] read file
# - [ ] end credits


import requests
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-l', '--list', type=str, required=True, help='IP list')

args = parser.parse_args()

url = 'https://api.abuseipdb.com/api/v2/check'

querystring = {
    'ipAddress': '20.161.75.217'
}

headers = {
    'Accept': 'application/json',
    'Key': 'a3649d5dbef218921e983faef320b81b5e52de714c30c268e4ab9a5abdb0a1086a12279d73be7a0d'
}

r = requests.get(url, headers=headers, params=querystring).json()

print(f"{r['data']['ipAddress']} was reported {r['data']['totalReports']} times. Confidence of Abuse is {r['data']['abuseConfidenceScore']}%")
