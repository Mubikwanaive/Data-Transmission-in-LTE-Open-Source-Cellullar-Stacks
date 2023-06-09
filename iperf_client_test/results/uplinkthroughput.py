
import matplotlib.pyplot as plt
import pandas as pd
distances = range(1, 11)  # Range of distances (1cm to 10cm)
throughput_table = pd.DataFrame(columns=distances)
allputs = []
# Iterate over the distances
for distance in distances:
    filename = f'iperf_results{distance}00cm.txt'

    # Read data from the file
    with open(filename, 'r') as file:
        lines = file.readlines()[1:]  # Skip the header line
        iterations = []
        transfers = []
        throughputs = []

        for line in lines:
            parts = line.strip().split("|")

            if len(parts[1]) >= 2:
                iteration = int(parts[0].strip())
                transfer = float(parts[1].strip().split()[4])
                throughput = float(parts[1].strip().split()[6])
                iterations.append(iteration)

                if parts[1].strip().split()[5] == 'KBytes':
                    transfer /= 1000    # Divide by 1000 if units are in Kbits/sec
                transfers.append(transfer)

                if parts[1].strip().split()[7] == 'Kbits/sec':
                    throughput /= 1000    # Divide by 1000 if units are in Kbits/sec
                throughputs.append(throughput)

        # Add throughput to the table
        throughput_table[distance] = pd.Series(throughputs)
        allputs.append(throughputs)
# Display the table
print(throughput_table)
#print(allputs)
# Create the plot
plt.boxplot(throughput_table.values, labels=throughput_table.columns, showfliers=False)
plt.xlabel("Distance (m)")
plt.ylabel("Uplink Throughput (Mbps)")
plt.title("Uplink Throughput Data Distribution by Distance")

# Display the values at min, max, and median of each box
for i, distance in enumerate(distances, start=1):
    values = throughput_table[distance]
    median = values.median()
    minimum = values.min()
    maximum = values.max()
    plt.text(i, maximum, f"Max: {maximum:.2f}", ha='center', va='bottom', color='red')
    plt.text(i, minimum, f"Min: {minimum:.2f}", ha='center', va='top', color='blue')
    plt.text(i, median, f"Median: {median:.2f}", ha='center', va='top', color='black')

# Display the box plot
plt.show()
