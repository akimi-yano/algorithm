# 59. Spiral Matrix II

# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

# Example:

# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix=[[0 for i in range (n)] for i in range(n)]
        

        top=left=0
        bottom=right=n-1
        count=1
    
        while count<n**2+1:
            for i in range(left,right+1):
                matrix[top][i]=count
                count+=1
            top+=1
            
            for i in range(top,bottom+1):
                matrix[i][right]=count
                count+=1
            right-=1

            for i in range(right,left-1,-1):
                matrix[bottom][i]=count
                count+=1
            bottom-=1

            for i in range(bottom,top-1,-1):
                matrix[i][left]=count
                count+=1
            left+=1
        
        return matrix

# sugoi solution

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        r, c, r_change, c_change = 0, 0, 0, 1
        for number in range(1, n*n+1):
            matrix[r][c] = number
            if matrix[(r+r_change)%n][(c+c_change)%n]:
                r_change, c_change = c_change, -r_change
            r += r_change
            c += c_change
        return matrix
    
# if square ahead of you is not empty, change direction
#   r_change, c_change
# 1     0         1   
# 2     1         0
# 3     0         -1
# 4     -1        0        