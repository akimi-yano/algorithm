# 1. Robot Paths
# Given a matrix of zeroes, determine how many unique paths exist from the top left corner to the bottom right corner.

 

# Input/Output

# Input: An array of an array if integers (matrix)

# Output: Integer

 

# Robot Paths Example

 

# Example 1:
#  Input:  
#  [[ 0, 0, 0, 0],
#   [ 0, 0, 0, 0],
#   [ 0, 0, 0, 0]]

#  Output: 38


# Example 2:

#  Input:  
#  [[ 0, 0, 0],
#   [ 0, 0, 0]]

#  Output: 4


# Example 3:
#  Input:  
#  [[ 0, 0, 0, 0, 0, 0, 0, 0],
#   [ 0, 0, 0, 0, 0, 0, 0, 0],
#   [ 0, 0, 0, 0, 0, 0, 0, 0],
#   [ 0, 0, 0, 0, 0, 0, 0, 0],
#   [ 0, 0, 0, 0, 0, 0, 0, 0]]

#  Output: 7110272


# From any point, you can travel in the four cardinal directions (north, south, east, west). A path is valid as long as it travels from the top left corner to the bottom right corner, does not go off of the matrix, and does not travel back on itself. Think of this as a graph traversal problem where you note the nodes you've visited in some way.

 


#
# Complete the 'robotPaths' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def robotPaths(matrix):

    def helper(x,y):
        if x>len(matrix)-1 or y>len(matrix[0])-1:
            return 0
        if x <0 or y <0:
            return 0
        if x==len(matrix)-1 and y == len(matrix[0])-1:
            return 1
        return helper(x+1,y) + helper(x,y+1) + helper(x-1,y) + helper(x,y-1)
    return helper(0,0)

