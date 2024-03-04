# Open the file
file = open("Day3/input.txt", "r")

def check_neighbours(matrix, first_elem, last_elem):
    asterisks = []
    # Check if there are symbols different from '.' and digits around the number
    for ineigh in range(first_elem[0]-1, last_elem[0]+2):
        for jneigh in range(first_elem[1]-1, last_elem[1]+2):
            # Check if the position is inside the matrix
            if (ineigh < 0 or ineigh >= len(matrix) or jneigh < 0 or jneigh >= len(matrix[0])) == False:
                if matrix[ineigh][jneigh] == '*':
                    asterisks.append((ineigh, jneigh))
    return asterisks

# Read the file and store each character as a matrix
matrix = []
for line in file:
    matrix.append(list(line.strip()))


# Get the numbers in the matrix
prev_digit = False
total_asterisks = []
for i,row in enumerate(matrix):
    for j,elem in enumerate(row):
        if elem.isdigit():
            if prev_digit == False: # First digit
                number = elem
                # Store first element position
                first_elem = (i,j)
                index_elem = (i,j)
                prev_digit = True
            elif j == len(row)-1: # Last digit
                number += elem
                index_elem = (i,j)
                prev_digit = False
                # Store last element position
                last_elem = index_elem
                # Get the asterisks around the number
                asterisks = check_neighbours(matrix, first_elem, last_elem)
                for asterisk_pos in asterisks:
                    total_asterisks.append([int(number), asterisk_pos])
            else:
                number += elem
                index_elem = (i,j)
                prev_digit = True
        else:
            if prev_digit == True: # Last digit
                # Store last element position
                last_elem = index_elem
                prev_digit = False
                # Get the asterisks around the number
                asterisks = check_neighbours(matrix, first_elem, last_elem)
                for asterisk_pos in asterisks:
                    total_asterisks.append([int(number), asterisk_pos])
               
                number = ''

sum = 0
# Multiply the numbers around the same asterisk and get its total sum
for i in range(len(total_asterisks)):
    for j in range(i+1, len(total_asterisks)):
        if total_asterisks[i][1] == total_asterisks[j][1]:
            sum += total_asterisks[i][0] * total_asterisks[j][0]
    
    


print('The total sum of valid elements is', sum)
