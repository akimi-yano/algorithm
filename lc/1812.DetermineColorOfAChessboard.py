# 1812. Determine Color of a Chessboard Square
# Easy

# 47

# 2

# Add to List

# Share
# You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.



# Return true if the square is white, and false if the square is black.

# The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second.

 

# Example 1:

# Input: coordinates = "a1"
# Output: false
# Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.
# Example 2:

# Input: coordinates = "h3"
# Output: true
# Explanation: From the chessboard above, the square with coordinates "h3" is white, so return true.
# Example 3:

# Input: coordinates = "c7"
# Output: false
 

# Constraints:

# coordinates.length == 2
# 'a' <= coordinates[0] <= 'h'
# '1' <= coordinates[1] <= '8'

# This solution works:

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        ROW = 8
        COL = 8
        val = 0
        matrix = [[0 for col in range(COL)] for row in range(ROW)]
        val = False
        for row in range(ROW):
            for col in range(COL):
                matrix[row][col] = val
                val = val ^ True
            val = val ^ True
        col, row = coordinates[0], coordinates[1]
        col = ord(col) - ord('a')
        row = int(row)-1
        return matrix[row][col]
                
# This solution works:

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        col, row = coordinates[0], coordinates[1]
        col = ord(col) - ord('a')
        row = int(row)
        return ((row + col) %2) == 0
                