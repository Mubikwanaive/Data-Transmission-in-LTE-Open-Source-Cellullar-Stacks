import matplotlib.pyplot as plt

distances = range(1, 11)  # Range of distances (1m to 10m)

# Create subplots
fig, axs = plt.subplots(5, 2, figsize=(12, 25))

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
    axs[i].plot(fps_values)
    axs[i].set_title(f'{distance}00cm')
    axs[i].set_xlabel('Measurement')
    axs[i].set_ylabel('FPS')

# Adjust spacing between subplots
plt.tight_layout()

# Show the plot
plt.show()
