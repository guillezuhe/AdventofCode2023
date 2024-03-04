# Open the file
file = open("Day3/input.txt", "r")

def check_neighbours(matrix, first_elem, last_elem):
    # Check if there are symbols different from '.' and digits around the number
    for ineigh in range(first_elem[0]-1, last_elem[0]+2):
        for jneigh in range(first_elem[1]-1, last_elem[1]+2):
            # Check if the position is inside the matrix
            if (ineigh < 0 or ineigh >= len(matrix) or jneigh < 0 or jneigh >= len(matrix[0])) == False:
                if matrix[ineigh][jneigh] != '.' and not matrix[ineigh][jneigh].isdigit():
                    return True
    return False

# Read the file and store each character as a matrix
matrix = []
for line in file:
    matrix.append(list(line.strip()))

sum = 0
# Get the numbers in the matrix
prev_digit = False
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
                # Check if there are symbols different from '.' and digits around the number
                if check_neighbours(matrix, first_elem, last_elem) == True:
                    sum += int(number)
            else:
                number += elem
                index_elem = (i,j)
                prev_digit = True
        else:
            if prev_digit == True: # Last digit
                # Store last element position
                last_elem = index_elem
                prev_digit = False
                # Check if there are symbols different from '.' and digits around the number
                if check_neighbours(matrix, first_elem, last_elem) == True:
                    sum += int(number)
               
                number = ''


print('The total sum of valid elements is', sum)
