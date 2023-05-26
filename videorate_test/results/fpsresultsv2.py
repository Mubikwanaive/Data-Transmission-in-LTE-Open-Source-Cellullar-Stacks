import matplotlib.pyplot as plt
import numpy as np

distances = range(1, 11)  # Range of distances (1m to 10m)

# Create subplots
fig, axs = plt.subplots(5, 2, figsize=(12, 10))

# Flatten the axs array for easier indexing
axs = axs.flatten()

# Iterate over the distances
for i, distance in enumerate(distances):
    filename = f'log{distance}00cm.txt'

    # Read data from the file
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Extract FPS values
    fps_values = []
    for line in lines:
        if line.startswith('Calculated FPS'):
            fps = float(line.split(':')[1].strip())
            fps_values.append(fps)

    # Plot line graph in the corresponding subplot
    axs[i].plot(fps_values, label='FPS')
    axs[i].axhline(y=np.mean(fps_values), color='red', linestyle='--', label='Average')
    avg = np.mean(fps_values)
    axs[i].text(i, avg, f"avg: {avg:.2f}", ha='center', va='top', color='black')
    axs[i].set_title(f'{distance}00cm')
    axs[i].set_xlabel('Measurement')
    axs[i].set_ylabel('FPS')
    axs[i].legend()

# Adjust spacing between subplots
plt.tight_layout()

# Show the plot
plt.show()
