#!/bin/bash
# isplays only the status code of the response
curl -s -o /dev/null "$1" -w "%{http_code}"
