# Open the file and read each line
file = open("Day1/input", "r")

digits_string = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def find_all_occurrences(s, sub):
    start = 0
    while True:
        start = s.find(sub, start)
        if start == -1: return
        yield start
        start += 1

sum = 0
for k, line in enumerate(file):
    number = 0
    first_digit_index = 99
    last_digit_index = 0
    # Look for the first number among the characters of the string
    for i in range(len(line)):
        if line[i].isdigit():
            first_digit_index = i
            first_digit = int(line[i])
            break
    # Look for the last number among the characters of the string
    for j in range(len(line) -1, -1, -1):
        if line[j].isdigit():
            last_digit_index = j
            last_digit = int(line[j])
            break

    for l1, digit in enumerate(digits_string):
        # Check if the digit is in the line and get its index
        for index in find_all_occurrences(line, digit):
            if index < first_digit_index:
                first_digit_index = index
                first_digit = l1 + 1

    for l2, digit in enumerate(digits_string):
        # Check if the digit is in the line and get its index
        for index in find_all_occurrences(line, digit):
            if index > last_digit_index:
                last_digit_index = index
                last_digit = l2 + 1
    
    number = first_digit * 10 + last_digit

    sum += number


file.close()

print("The sum of the numbers is: ", sum)


   
