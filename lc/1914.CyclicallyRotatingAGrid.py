# 1914. Cyclically Rotating a Grid
# Medium

# 117

# 193

# Add to List

# Share
# You are given an m x n integer matrix grid​​​, where m and n are both even integers, and an integer k.

# The matrix is composed of several layers, which is shown in the below image, where each color is its own layer:



# A cyclic rotation of the matrix is done by cyclically rotating each layer in the matrix. To cyclically rotate a layer once, each element in the layer will take the place of the adjacent element in the counter-clockwise direction. An example rotation is shown below:


# Return the matrix after applying k cyclic rotations to it.

 

# Example 1:


# Input: grid = [[40,10],[30,20]], k = 1
# Output: [[10,20],[40,30]]
# Explanation: The figures above represent the grid at every state.
# Example 2:

  
# Input: grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
# Output: [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
# Explanation: The figures above represent the grid at every state.
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 2 <= m, n <= 50
# Both m and n are even integers.
# 1 <= grid[i][j] <= 5000
# 1 <= k <= 109

# This solution works:

class Solution:
    def assign(self, temp, rows, cols, i, j, arr, topL, topR, bottomR, bottomL):
        ix = 0
        # top row
        while j < topR[1]:
            temp[i][j] = arr[ix]
            ix += 1
            j += 1

        # last column
        while i < bottomR[0]:
            temp[i][j] = arr[ix]
            ix += 1
            i += 1

        # last row
        while j > bottomL[1]:
            temp[i][j] = arr[ix]
            ix += 1
            j -= 1

        # first column
        while i > topR[0]:
            temp[i][j] = arr[ix]
            ix += 1
            i -= 1

        
    
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols, i, j = len(grid), len(grid[0]), 0, 0
		# Marking the 4 points, which will act as boundaries
        topLeft, topRight, bottomRight, bottomLeft = [0,0],[0,cols-1],[rows-1, cols-1],[rows-1, 0]
        temp = [[-1 for _ in range(cols)] for __ in range(rows) ] 
        while topLeft[0] < rows//2 and topLeft[0] < cols//2:
            arr = []
            # top row
            while j < topRight[1]:
                arr.append(grid[i][j])
                j += 1

            # last column
            while i < bottomRight[0]:
                arr.append(grid[i][j])
                i += 1
                
            # last row
            while j > bottomLeft[1]:
                arr.append(grid[i][j])
                j -= 1
            
            # first column
            while i > topRight[0]:
                arr.append(grid[i][j])
                i -= 1

            n = len(arr)
            arr = arr[k % n:] + arr[:k % n] # Taking modulus value
            
            
            self.assign(temp, rows, cols, i, j, arr,topLeft, topRight, bottomRight, bottomLeft )
            
            i += 1
            j += 1
            topLeft[0] += 1
            topLeft[1] += 1
            topRight[0] += 1
            topRight[1] -= 1
            bottomRight[0] -= 1
            bottomRight[1] -= 1
            bottomLeft[0] -= 1
            bottomLeft[1] += 1
            
        
        return temp