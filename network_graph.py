import csv
from datetime import datetime
import matplotlib.pyplot as plt

timestamps = []
rtts = []

with open('network_data.csv', 'r') as file:
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
                
plt.plot(timestamps, rtts)
plt.xlabel('Timestamp')
plt.ylabel('Round-trip Time (ms)')
plt.title('Network Stability')
plt.show()
