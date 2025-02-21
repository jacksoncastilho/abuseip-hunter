#! /usr/bin/bash

readonly API_KEY=a0d3bd68be14eedf6264ee5a66cec5bdb49ca2c5d3612d7c40a2725776d321233ac380ec196b8e17

curl -G https://api.abuseipdb.com/api/v2/check \
  --data-urlencode "ipAddress=$1" \
  -H "Key: $API_KEY" \
  -H "Accept: application/json"
