# Read the file
with open("Day8/input.txt", "r") as file:
    data = file.readlines()

# The first line is the left right instructions
lr = data[0].strip()

print(lr)

# The rest of the lines are the instructions
data = data[2:]

# Each line has the format AAA = (BBB, CCC)
# Record the values of AAA, BBB, and CCC
net = []
for line in data:
    line = line.strip().split(" ")
    net.append((line[0], line[2][1:4], line[3][0:3]))
    print(net[-1])

# Look for 'AAA' in the net
found = False
target = 'AAA'
step = 0
index = 0

while not found:
    # Look for target in the net
    if target == 'ZZZ':
        print('Reached the end of the net')
        found = True
        break
    for i in range(len(net)):
        if net[i][0] == target:
            # Get if we should read the left or right value
            if lr[index] == 'L':
                target = net[i][1]
            else:
                target = net[i][2]
        
            print(target, lr[index])
            index = (index + 1) % len(lr)
            step += 1
            
            break

print('Number of steps:', step)