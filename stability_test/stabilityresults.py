import subprocess
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import os

distances = range(1, 11)

# Create a 2x5 grid of subplots
fig, axes = plt.subplots(2, 5, figsize=(16, 8))
fig.subplots_adjust(hspace=0.5)  # Adjust the vertical spacing between subplots

for i, distance in enumerate(distances):
    filename = f'{distance}00cmduringiperf.pcapng'
    output_file = f'network_data_{distance}00cm.csv'

    # Check if the output file already exists
    if os.path.isfile(output_file):
        print(f"Using existing file: {output_file}")
    else:
        # Run tshark command to extract timestamps and RTTs
        command = f"tshark -r {filename} -T fields -e frame.time_epoch -e tcp.analysis.ack_rtt -E header=y -E separator=, -E quote=d"
        output = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Save the output to the CSV file
        with open(output_file, 'w') as file:
            file.write(output.stdout)

    # Read the CSV file and generate the graph
    timestamps = []
    rtts = []

    with open(output_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if len(row) >= 2 and row[1]:  # Check if the row has at least two columns and the second column is not empty
                try:
                    timestamp = float(row[0])
                    rtt = float(row[1])
                    timestamps.append(datetime.fromtimestamp(timestamp))
                    rtts.append(rtt)
                except ValueError:
                    print(f"Skipping invalid row: {row}")

    # Plot the graph in the corresponding subplot
    row = i // 5  # Calculate the row index
    col = i % 5  # Calculate the column index
    ax = axes[row, col]
    ax.plot(timestamps, rtts)
    ax.axhline(y=3, color='red', linestyle='--')  # Draw a horizontal line at RTT=3
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Round-trip Time (ms)')
    ax.set_title(f'Network Stability for {distance}00cm')

# Display the subplots
plt.tight_layout()
plt.show()
