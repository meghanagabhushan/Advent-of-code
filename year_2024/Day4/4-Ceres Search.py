import sys
import os
import re
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import utils
matrix = utils.read_file_into_matrix("input2.txt")



pattern = r'XMAS'

def main():

    total = 0

    #Horizontal
    for row in matrix:
        total+= len(re.findall(pattern, "".join(row)))
        total+= len(re.findall(pattern, "".join(row[::-1])))

    #Vertical
    for j in range(len(matrix[0])):
        column = [matrix[i][j] for i in range(len(matrix))]
        total += len(re.findall(pattern, "".join(column)))
        total += len(re.findall(pattern, "".join(column[::-1])))

    #Diagonal
    for i in range(len(matrix) - 3) :
        for j in range(len(matrix[0]) -3) : 
            miniTable = []

            for x in range(4) : 
                row = []
                for y in range(4) : 
                    row.append(matrix[i+x][j+y])
                miniTable.append(row)

            main_diagonal = [miniTable[k][k] for k in range(4)]
            anti_diagonal = [miniTable[k][3-k] for k in range(4)]

            total += len(re.findall(pattern, "".join(main_diagonal)))
            total += len(re.findall(pattern, "".join(main_diagonal[::-1])))

            total += len(re.findall(pattern, "".join(anti_diagonal)))
            total += len(re.findall(pattern, "".join(anti_diagonal[::-1])))
    print(total)

    ##### PART 2 #####  
    #create a 3*3 matrix and look for both diagonals similar to the last one
    total2 = 0
    for i in range(len(matrix) - 2) :
        for j in range(len(matrix[0]) -2) : 
            miniTable = []

            for x in range(3) : 
                row = []
                for y in range(3) : 
                    row.append(matrix[i+x][j+y])
                miniTable.append(row)

            main_diagonal = [miniTable[k][k] for k in range(3)]
            anti_diagonal = [miniTable[k][2-k] for k in range(3)]

            main_str = "".join(main_diagonal)
            anti_str = "".join(anti_diagonal)

            values = ["MAS","SAM"]

            if main_str in values and anti_str in values:
                total2+=1

    print(total2)



main()

