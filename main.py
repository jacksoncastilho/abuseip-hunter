import requests
import argparse
import sys
import yaml
import re
from pathlib import Path

def getApi():
    try:
        f = open('./api.yaml', 'r')

        api = yaml.safe_load(f)

        f.close()

        return api
    except Exception as err:
        print(f"An exception occurred!\n{err}")

def checkIpReputation(ip, api):
    headers = {
        'Accept': 'application/json',
        'Key': api['key']
    }

    try:
        resp = requests.get(api['url'], headers=headers, params={'ipAddress': ip})
    except requests.exceptions.RequestException as err:
        print(f"An exception occurred!\n{err}")
    
    if resp.status_code == 200:
        data = resp.json()
        print(f"{data['data']['ipAddress']} was reported {data['data']['totalReports']} times. Confidence of Abuse is {data['data']['abuseConfidenceScore']}%")
    else:
        print(f"An exception occurred!\nCheck your YAML file")
        exit()

def byFile():
    try:
        ips = open(args.ip, 'r')
        
        for ip in ips:
            for apis in getApi()['apis']:
                for api in apis.keys():
                    checkIpReputation(ip, apis[api])

        ips.close()
    except Exception as err:
        print(f"An exception occurred!\n{err}")

def byIp():
    for apis in getApi()['apis']:
            for api in apis.keys():
                checkIpReputation(args.ip, apis[api])

parser = argparse.ArgumentParser()
parser.add_argument('-ip', type=str, required=True, help='Enter a file or an IP')

args = parser.parse_args()

if Path(args.ip).exists() and Path(args.ip).is_file():
    byFile()
elif re.fullmatch(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", args.ip):
    byIp()
else:
    raise Exception(f"An exception occurred!\nThe IP or file does not exist")