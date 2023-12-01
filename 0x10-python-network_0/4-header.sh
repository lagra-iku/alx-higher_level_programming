#!/bin/bash
#a Bash script that takes in a URL as an argument, sends a GET request to the URL
#A header variable X-School-User-Id must be sent with the value 98
curl -sHX GET "X-School-User-Id: 98" "$1"
