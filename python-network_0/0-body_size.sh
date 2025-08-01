#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 <URL>" >&2
  exit 1
fi

# Fetch the body silently and count bytes
curl -s "$1" | wc -c
