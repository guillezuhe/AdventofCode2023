import numpy as np

# Open the file
file = open("Day4/input.txt", "r")
# Get the len of the file
file_len = len(file.readlines())
file.close()

copies = np.ones(file_len, dtype=int)

file = open("Day4/input.txt", "r")

# Read the file
points = 0
for k, line in enumerate(file):
    # Read the winning numbers
    winning_numbers = line.strip().split(':')[1].strip().split('|')[0].strip().split()
    winning_numbers = [int(x) for x in winning_numbers]
    # Read the numbers i have
    numbers = line.strip().split(':')[1].strip().split('|')[1].strip().split()
    numbers = [int(x) for x in numbers]

    # Check how many winning numbers i have
    count = 0
    for number in numbers:
        if number in winning_numbers:
            count += 1

    for i in range(k + 1, k + 1 + count):
        copies[i] += 1 * copies[k]

print('Total points:', np.sum(copies))


