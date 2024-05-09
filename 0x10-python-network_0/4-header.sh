#!/bin/bash
# Sends a GET request to the URL, and displays the body of the response
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

curl -sH "X-HolbertonSchool-User-Id: 98" "${1}"
