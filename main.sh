#! /usr/bin/bash

readonly API_KEY=#api_key_here!

_check(){
    local response=$(curl -G -s https://api.abuseipdb.com/api/v2/check \
      --data-urlencode "ipAddress=$1" \
      -H "Key: $API_KEY" \
      -H "Accept: application/json")

    local totalReports=$(echo $response | egrep -o "\"totalReports\":[0-9]+," | egrep -o "[0-9]+")

    local abuseConfidenceScore=$(echo $response | egrep -o "\"abuseConfidenceScore\":[0-9]+," | egrep -o "[0-9]+")

    [[ $totalReports -gt 0 ]] && echo "$1 was found in our database with score $abuseConfidenceScore%"
}

for ip in $(cat $1); do
    _check $ip
done
