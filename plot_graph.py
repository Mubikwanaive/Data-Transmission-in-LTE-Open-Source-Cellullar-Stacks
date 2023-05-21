import matplotlib.pyplot as plt

# Define the dataset
dataset = {
    "50cm": [
        [0.0000, 10.1745, 15.8, 13.0],
        [0.0000, 14.5595, 11.5, 6.63],
        [0.0000, 10.2305, 21.5, 17.6],
        [0.0000, 10.6430, 20.9, 16.5],
        [0.0000, 13.4492, 9.08, 5.67],
        [0.0000, 10.1785, 23.3, 19.2],
        [0.0000, 10.9055, 20.8, 16.0],
        [0.0000, 10.3102, 23.4, 19.0],
        [0.0000, 14.5576, 11.7, 6.74],
        [0.0000, 10.2188, 20.3, 16.6],
        [0.0000, 10.2012, 12.8, 10.5],
        [0.0000, 13.2830, 6.61, 4.18]
    ],
    "100cm": [
        [0.0000, 10.0740, 8.75, 7.29],
        [0.0000, 10.6660, 10.1, 7.96],
        [0.0000, 10.8949, 4.63, 3.56],
        [0.0000, 10.8634, 7.50, 5.79],
        [0.0000, 12.2376, 2.25, 1.54],
        [0.0000, 10.1434, 10.1, 8.37],
        [0.0000, 10.0156, 12.5, 10.5],
        [0.0000, 10.5876, 20.5, 16.2],
        [0.0000, 13.1172, 5.59, 3.58],
        [0.0000, 10.1378, 13.3, 11.0],
        [0.0000, 11.0116, 20.1, 15.3],
        [0.0000, 13.3681, 3.11, 1.95]
    ],
    "200cm": [
        [0.0000, 11.5733, 2.96, 2.14],
        [0.0000, 11.0252, 1.00, 0.761],
        [0.0000, 10.2585, 3.00, 2.45],
        [0.0000, 11.3773, 4.14, 3.05],
        [0.0000, 10.5371, 5.63, 4.48],
        [0.0000, 10.1829, 3.00, 2.47],
        [0.0000, 12.9222, 2.48, 1.61],
        [0.0000, 12.0502, 1.16, 0.805],
        [0.0000, 10.1638, 7.00, 5.78],
        [0.0000, 10.6015, 4.75, 3.76],
        [0.0000, 10.1486, 5.75, 4.75],
        [0.0000, 12.7109, 2.01, 1.33]
    ]
}

# Extract the throughput values for each distance
distances = list(dataset.keys())
throughputs = {distance: [] for distance in distances}
for distance, data_points in dataset.items():
    for data_point in data_points:
        throughputs[distance].append(data_point[3])

# Plot the graph
for distance in distances:
    plt.plot(range(1, len(throughputs[distance]) + 1), throughputs[distance], marker='o', label=distance)

# Calculate average throughput for each distance
average_throughputs = {distance: sum(throughputs[distance]) / len(throughputs[distance]) for distance in distances}

# Add average throughput text to the plot
for distance in distances:
    plt.text(len(throughputs[distance]), throughputs[distance][-1], f"Avg: {average_throughputs[distance]:.2f} Mbps",
             verticalalignment='bottom', horizontalalignment='right')

plt.xlabel("Iteration")
plt.ylabel("Throughput (Mbps)")
plt.title("iPerf Throughput Results")
plt.legend()
plt.grid(True)

# Display the graph
plt.show()


