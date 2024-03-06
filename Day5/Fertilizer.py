import numpy as np

# Open the input file
file = open("Day5/input.txt", "r")

# Read the file
data = file.readlines()

#print(data)

# The first line of the input file contains the seeds

seeds = data[0].strip().split(":")[1].strip().split(" ")
seeds = [int(x) for x in seeds]

print('Seeds', seeds)


# Read the maps
# Each map is separated by a blank line and has a title line
maps = []
map = []
for line in data[2:]:
    if line.strip() == "":
        maps.append(map)
        map = []
    # Check if we are at the last line
    elif data.index(line) == len(data)-1:
        map.append([int(x) for x in line.strip().split('\n')[0].strip().split(" ")])
        maps.append(map)
    # Check if the line is a title
    elif line.strip().split(" ")[0].isdigit() == False:
        # It is a title, so we skip it
        continue
    else:
        map.append([int(x) for x in line.strip().split('\n')[0].strip().split(" ")])


# Now we have the seeds and the maps and we can start the transformation process
mapped = seeds

for k in range(len(mapped)):
    for map in maps:
        for range_ in map:
            # Get the source range start
            source_start = range_[1]
            destination_start = range_[0]
            range_len = range_[2]

            if mapped[k] >= source_start and mapped[k] < (source_start + range_len):
                mapped[k] = destination_start + (mapped[k] - source_start)
                break

    print('Mapped', mapped)

# Look for the minimum of the last mapped values
print('Minimum', min(mapped))