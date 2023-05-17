#!/bin/bash

sudo netstat -lpn | grep :2222 > /dev/null

if [ $? -eq 0 ]; then
    echo "Port 2222 is in use. Killing process..."
    sudo kill -9 $(sudo lsof -t -i:2222)
else
    echo "Port 2222 is free."
fi

while true; do
  if ssh pi@localhost -p 2222 -X; then
    break
  else
    echo "Failed to connect. Retrying in 5 seconds..."
    sleep 5
  fi
done
