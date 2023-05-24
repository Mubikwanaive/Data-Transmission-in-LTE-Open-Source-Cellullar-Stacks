#!/bin/bash

# Define the remote server and port for the reverse SSH tunnel
remote_user="wanga"
remote_host="172.16.0.1"
remote_port="2222"

# Function to establish the reverse SSH tunnel
function establish_tunnel {
  autossh -N -T -R ${remote_port}:localhost:22 ${remote_user}@${remote_host}
  echo "Reverse SSH tunnel terminated. Trying to reconnect in 3 seconds..."
 # sleep 3
}

# Main loop to continuously check the network status and establish the tunnel if necessary
while true; do
  # Check the network status by pinging a reliable host
  echo "ping testing host"
  if ping -q -c 1 -W 3 172.16.0.1 >/dev/null; then
    # Network is up, so establish the tunnel
    echo "hello"
    establish_tunnel &    # run function in the background
    tunnel_pid=$!         # get the PID of the background process
    wait $tunnel_pid      # Wait for the background process to complete
  else
    # Network is down, so wait a few seconds and check again
    echo "Network connection lost. Waiting 5 seconds to check again..."
    sleep 3
  fi
done
