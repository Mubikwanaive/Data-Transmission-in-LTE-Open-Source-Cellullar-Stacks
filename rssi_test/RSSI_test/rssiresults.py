import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
distances = range(1, 11)  # Range of distances (1cm to 10cm)
rssi_table = pd.DataFrame(columns=["Distance", "RSSI"])

# Iterate over the distances
for distance in distances:
    filename = f'logged{distance}00cm.txt'

    # Read data from the file
    with open(filename, 'r') as file:
        lines = file.readlines()
        rssi_values = []
        for line in lines:
            parts = line.strip().split(" ")
            if len(parts) >= 4 and parts[4] == "RSSI:":
                rssi = int(parts[5])
                rssi_values.append(rssi)

        # Add the RSSI values to the table
        rssi_table.loc[distance] = [distance, rssi_values]

print(rssi_table)
# RSSI Box Plot
plt.boxplot(rssi_table["RSSI"], labels=rssi_table["Distance"],showfliers=False)
plt.xlabel("Distance (m)")
plt.ylabel("RSSI value")
plt.title("RSSI Distribution by Distance")

# Calculate and display the values at min, max, and median
for i, distance in enumerate(distances):
    filtered_data = rssi_table[rssi_table["Distance"] == distance]
    values = [item for sublist in filtered_data["RSSI"].values for item in sublist]
    print(values)
    rssi_values = np.array(values)
    #median = values.median()
    #minimum = values.min()
    #maximum = values.max()
    #plt.text(i, maximum, f"Max: {maximum:.2f}", ha='center', va='bottom', color='red')
    #plt.text(i, minimum, f"Min: {minimum:.2f}", ha='center', va='top', color='blue')
    #plt.text(i, median, f"Median: {median:.2f}", ha='center', va='top', color='black')
    min_val = np.min(rssi_values)
    max_val = np.max(rssi_values)
    print(max_val)
    median_val = np.median(rssi_values)
    plt.text(i+1, min_val, str(min_val), ha="center", va="bottom")
    #plt.text(i+1, max_val, str(max_val), ha="center", va="top")
    plt.text(i+1, median_val, str(median_val), ha="center", va="bottom")

# Display the box plots
plt.show()
