#! /usr/bin/bash

readonly API_KEY=a3649d5dbef218921e983faef320b81b5e52de714c30c268e4ab9a5abdb0a1086a12279d73be7a0d

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
