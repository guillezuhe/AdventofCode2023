import numpy as np

# Open the input file
file = open("Day6/input.txt", "r")

data = file.readlines()

# Remove white spaces in the first line and join all the numbers together


times = data[0].strip().split(':')[1].strip().replace(' ', '').replace('\n', '')
times = [int(times)]

distances = data[1].strip().split(':')[1].strip().replace(' ', '').replace('\n', '')
distances = [int(distances)]

print(times, distances)

# Velocity constant
k = 1

margin = 1
# Calculate the minimum pressing time solving the inequality
# dmin < k*t*ti - k*ti^2
for t, d in zip(times, distances):
    t1 = (k * t - np.sqrt(k*k*t*t - 4*k*d)) / (2*k) + 1e-6 # This las term is to avoid exact integers
    t2 = (k * t + np.sqrt(k*k*t*t - 4*k*d)) / (2*k) - 1e-6

    # t1 is the minimum time, get the higher integer
    t1_r = int(np.ceil(t1))
    # t2 is the maximum time, get the lower integer
    t2_r = int(np.floor(t2))

    print(t1, t2, 'margin', (t2_r - t1_r + 1))

    margin *= (t2_r - t1_r + 1)

print('Margin of error', margin)