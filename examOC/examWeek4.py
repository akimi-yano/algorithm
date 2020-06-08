
# 1. Rover Control
# You are working on a Mars rover project. 
# Your job is to control the rover's movement on a square matrix. 
# Your code accepts a sequence of commands to move the rover in any of the four directions from each cell: 
# [UP, DOWN, LEFT or RIGHT]. You may NOT move diagonally or outside the boundary. 
# The rover starts from cell 0.

# Each cell in the matrix has a position equal to:
# (row * size) + column
# where row and column are zero-indexed, size = row length of the matrix. 

# Return the final position of the rover after all moves.

# Example: commands = [RIGHT, UP, DOWN, LEFT, DOWN, DOWN] and matrix size = 4.  Rover path is shown below. 

#     RIGHT: Rover moves to position 1

#     UP: Position unchanged, as the move would take the rover out of the boundary.

#     DOWN: Rover moves to Position 5. 

#     LEFT: Rover moves to position 4

#     DOWN: Rover moves to position 8

#     DOWN: The rover ends up in position 12. 

# The function must return 12.


# Function Description 

# Complete the function roverMove in the editor below. The function must return the label of the cell the rover occupies after executing all commands.



# roverMove has the following parameter(s):

#     n: an integer that represents the size of the square matrix

#     cmds[cmds[0],...cmds[m-1]]:  an array of strings that represent the commands



# Constraints

# 2 ≤ n ≤ 20
# 1 ≤ | cmds | ≤ 20
 

# Input Format For Custom Testing
# Sample Case 0
# Sample Input 0:

# 4
# 5 (commands)
# RIGHT
# DOWN
# LEFT
# LEFT
# DOWN

# >>8
 

# Explanation 0

# Rover starts at position 0

# RIGHT  → pos 1

# DOWN → pos 5

# LEFT → pos 4

# LEFT → pos 4, No effect

# DOWN → pos 8


# A 4x4 matrix, labeled
# 0	1	2	3
# 4	5	6	7
# 8	9	10	11
# 12	13	14	15


# Complete the 'roverMove' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER matrixSize
#  2. STRING_ARRAY cmds



def roverMove(matrixSize, cmds):
    max_row = matrixSize-1
    max_col = matrixSize-1
    cur_row = 0
    cur_col = 0
    for cmd in cmds:
        if cmd == "RIGHT" and cur_col!=max_col:
            cur_col+=1
        if cmd == "LEFT" and cur_col!=0:
            cur_col-=1
        if cmd == "UP" and cur_row!=0:
            cur_row-=1
        if cmd == "DOWN" and cur_row!=max_row:
            cur_row+=1
    return cur_row*matrixSize + cur_col

print("Problem 1 - rover_move:", roverMove(4,['RIGHT','DOWN', 'LEFT', 'LEFT', 'DOWN'])) 
# Expected to return 8


# 2. Simple Matrix Summation
# Given an n x m matrix, a, where each a(i, j) is the value of the cell at the intersection of 
# row i and column j, create another n x m matrix, b, using the following algorithm to set the 
# values of each b(x, y) with zero-based indexing:



# s = 0;

# for (i = 0; i ≤ x; i += 1) {
#     for (j = 0; j ≤ y; j += 1) {
#         s = s + a(i, j);
#     }
# }

# b(x, y) = s;


# Note that the algorithm sets just one b(x, y) per execution and that 0 ≤ x < n and 0 ≤ y < m. 
# It should be run for each element of b. Return the completed n × m matrix b.



# Example

# If matrix a is:

# 1 2 3
# 4 5 6
# The following operations are performed:

# Element 	Equation 		Values		b(x, y)
# -------		-----------------------	-------------	------
# b(0,0)		a(0,0)			1		1
# b(0,1)		a(0,0)+a(0,1)		1+2		3
# b(0,2)		a(0,0)+a(0,1)+a(0,2) 	1+2+3		6
# b(1,0)		a(0,0)+a(1,0)		1+4		5
# b(1,1)		a(0,0)+a(0,1)		1+2+4+5		12
# 		+a(1,0)+a(1,1)
# b(1,2)		a(0,0)+a(0,1)+a(0,2)	1+2+3+4+5+6	21
# 		+a(1,0)+a(1,1)+a(1,2)
# The final matrix b is:

# 1  3  6
# 5 12 21


# Function Description

# Complete the function findMatrix in the editor below.



# findMatrix has the following parameter(s):

#     a[a[0],...a[n-1]]: a 2-dimensional array of integers



# Returns:

#     int[]: an n x m(2-dimensional) matrix of integers denoting b 



# Constraints

# 1 ≤ n, m ≤ 103
# 0 ≤ a(i, j) ≤ 103, where 0 ≤ i < n and 0 ≤ j < m.
# Input Format for Custom Testing
# Sample Case 0
# Sample Input

# STDIN     Function
# -----     -----
# 2      →  number of rows in a[] n = 2
# 2      →  number of columns in a[] m = 2
# 1 2    →  first row of a[] = [1, 2]
# 3 4    →  second row of a[] = [3, 4]


# Sample Output

# 1 3
# 4 10


# Explanation

# Find the following 2 × 2 matrix, b:

# b(0, 0) = a(0, 0) = 1
# b(0, 1) = a(0, 0) + a(0, 1) = 1 + 2 = 3
# b(1, 0) = a(0, 0) + a(1, 0) = 1 + 3 = 4
# b(1, 1) = a(0, 0) + a(0, 1) + a(1, 0) + a(1, 1) = 1 + 2 + 3 + 4 = 10



# Complete the 'findMatrix' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY a as parameter.




def findMatrix(a):
    b = a
    for row in range(len(b)):
        for col in range(len(b[row])):
        
            if row!=0 and col!=0:
                b[row][col]+=(b[row-1][col]+b[row][col-1]-b[row-1][col-1])
            elif row != 0:
                b[row][col]+=b[row-1][col]
            elif col != 0:
                b[row][col]+=b[row][col-1]
    return b
print("Problem 2 - find_matrix:",findMatrix([[1,2,3],[4,5,6]]))
# Expected to return [[1, 3, 6], [5, 12, 21]]