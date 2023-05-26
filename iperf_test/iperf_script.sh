#!/bin/bash

# Number of iterations
iterations=15

# Output file
output_file="iperf_results.txt"

# Header
echo "Iteration | Throughput (Mbps)" > $output_file

# Run iPerf multiple times
for ((i=1; i<=$iterations; i++))
do
    echo "Running iteration $i..."
    #run ierf in the akground nd redirect output to the temporary file
    (iperf -c 172.16.0.1 | awk '/0.0000-/{print $i}') > temp_result.txt & 
    iperf_pid=$! #get the proces ID

    #wait for the iperf command to complete
    wait $iperf_pid

    #Read the rsut from the temporary file
    result=$(cat temp_result.txt)
    echo "Throughput: $result"
    echo "$i | $result" >> $output_file

done
#Remove the temporary fle
rm temp_result.txt

echo "Done! Results saved to $output_file."
