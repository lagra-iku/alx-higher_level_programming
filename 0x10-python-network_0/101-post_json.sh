#!/bin/bash
# send a JSON POST
curl -sd "@$2" -X POST -H "Content-Type: application/json" "$1"
