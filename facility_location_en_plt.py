import matplotlib.pyplot as plt

# Machine coordinates and number of trips
machines = [
    {"coordinates": (8, 5), "trips": 9},
    {"coordinates": (4, 2), "trips": 6},
    {"coordinates": (11, 8), "trips": 4},
    {"coordinates": (13, 2), "trips": 12}
]

# Separating X and Y coordinates and weights
x_coords = [machine["coordinates"][0] for machine in machines]
y_coords = [machine["coordinates"][1] for machine in machines]
weights = [machine["trips"] for machine in machines]

# Total of weights
total_weight = sum(weights)
half_weight = total_weight / 2

# Function to calculate weighted median
def weighted_median(coords, weights):
    sorted_pairs = sorted(zip(coords, weights))
    sorted_coords, sorted_weights = zip(*sorted_pairs)

    cumulative_weight = 0
    for i in range(len(sorted_weights)):
        cumulative_weight += sorted_weights[i]
        if cumulative_weight >= half_weight:
            return sorted_coords[i]

# Finding the median for X and Y coordinates
x_star = weighted_median(x_coords, weights)
y_star = weighted_median(y_coords, weights)

# Print the results
print(f"The location of the new facility: ({x_star}, {y_star})")

# Visualization
plt.figure(figsize=(10, 6))

# Plotting machines as points
plt.scatter(x_coords, y_coords, s=[w * 20 for w in weights], alpha=0.5, color='blue', label='Machines')

# Plotting the new facility location
plt.scatter(x_star, y_star, s=200, color='red', label='New Facility', edgecolor='black')

# Graph settings
plt.title('Machine Locations and New Facility Location')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.xlim(0, 15)
plt.ylim(0, 10)
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.legend()
plt.show()
