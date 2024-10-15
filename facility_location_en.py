# Question: Machines 1, 2, 3, and 4 are located at (8, 5), (4, 2), (11, 8), and (13, 2) respectively. 
# The number of trips between the machines and a new facility is 9, 6, 4, and 12 trips per week respectively. 
# Based on this, where should the new facility be located?

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

# Weighted median for X
def weighted_median(coords, weights):
    # Combine and sort coordinates and weights
    sorted_pairs = sorted(zip(coords, weights))
    sorted_coords, sorted_weights = zip(*sorted_pairs)

    cumulative_weight = 0
    for i in range(len(sorted_weights)):
        cumulative_weight += sorted_weights[i]
        if cumulative_weight >= half_weight:
            return sorted_coords[i]  # Return the first coordinate that exceeds half the weight

# Finding the median for X and Y coordinates
x_star = weighted_median(x_coords, weights)
y_star = weighted_median(y_coords, weights)

# Print the results
print(f"The location of the new facility: ({x_star}, {y_star})")
