# Open the file and read each line
file = open("Day1/input", "r")
output = open("Day1/output", "w")

sum = 0
for k, line in enumerate(file):
    number = 0
    # Look for the first number among the characters of the string
    for i in range(len(line)):
        if line[i].isdigit():
            number += 10 * int(line[i])
            break
    # Look for the last number among the characters of the string
    for j in range(len(line) -1, -1, -1):
        if line[j].isdigit():
            number += int(line[j])
            break
    sum += number
    #print('Line', k, ':  ', number)
    output.write(str(number)+'\n')

file.close()
output.close()

print("The sum of the numbers is: ", sum)


   
