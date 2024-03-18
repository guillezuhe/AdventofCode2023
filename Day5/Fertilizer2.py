import numpy as np

# Open the input file
file = open("Day5/input.txt", "r")

# Read the file
data = file.readlines()

#print(data)

# The first line of the input file contains the seed ranges
seeds_builder = data[0].strip().split(":")[1].strip().split(" ")
seeds_builder = [int(x) for x in seeds_builder]



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
#mapped = seeds
mins = []

for i in range(0, len(seeds_builder), 2):
    (ss, se) = (seeds_builder[i], seeds_builder[i] + seeds_builder[i+1]) # Seed start and end
    R = [(ss, se)]
    for map in maps:
        A = []
        for range_ in map:
            NR = []
            # Get the source range start
            source_start = range_[1]
            destination_start = range_[0]
            range_len = range_[2]

            # Range
            (rs, re) = (source_start, source_start + range_len)
            # Mapped range
            (ms, me) = (destination_start, destination_start + range_len)

            # Explore the three intervals
            # 1. Before the source range
            before = (ss, min(rs, se))
            # 2. The source range
            inter = (max(ss, rs), min(se, re))
            # 3. After the source range
            after = (max(ss, re), se)

            if before[1] > before[0]:
                NR.append(before)
            if inter[1] > inter[0]:
                A.append((inter[0]-rs+ms, inter[1]-rs+ms))
            if after[1] > after[0]:
                NR.append(after)

            R = NR
        
        A = A + R

            

            

            



    if mapped < min_mapped:
        min_mapped = mapped

    #print('Mapped', mapped)

# Look for the minimum of the last mapped values
print('Minimum', min_mapped)