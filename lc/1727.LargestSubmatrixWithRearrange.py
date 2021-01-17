# 1727. Largest Submatrix With Rearrangements
# Medium

# 32

# 2

# Add to List

# Share
# You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.

# Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.



# Example 1:



# Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
# Output: 4
# Explanation: You can rearrange the columns as shown above.
# The largest submatrix of 1s, in bold, has an area of 4.
# Example 2:



# Input: matrix = [[1,0,1,0,1]]
# Output: 3
# Explanation: You can rearrange the columns as shown above.
# The largest submatrix of 1s, in bold, has an area of 3.
# Example 3:

# Input: matrix = [[1,1,0],[1,0,1]]
# Output: 2
# Explanation: Notice that you must rearrange entire columns, and there is no way to make a submatrix of 1s larger than an area of 2.
# Example 4:

# Input: matrix = [[0,0],[0,0]]
# Output: 0
# Explanation: As there are no 1s, no submatrix of 1s can be formed and the area is 0.


# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m * n <= 105
# matrix[i][j] is 0 or 1.


# This approach does not work
# class Solution:
#     def largestSubmatrix(self, matrix: List[List[int]]) -> int:
#         if matrix is None or matrix[0] is None:
#             return 0
#         M = len(matrix)
#         N = len(matrix[0])
#         for col in range(N):
#             for row in range(M):
#                 print(matrix[row][col])

# Example 1

# [0,0,1],
# [1,1,1],
# [1,0,1]

# For every column, we count the the number of continuous 1 by the current position. the result matrix will be

# [0,0,1],
# [1,1,2],
# [2,0,3]

# Now let’s consider every row.
# For the first row, we reversely sort the row
# We got [1,0,0]. It's very easy to get the largest matrix for this row. For other rows, we do the same thing.

# For example, for the second row, We reversely sort the row,
# [2,1,1]
# For the third row, We reversely sort the row,
# [3,2,0]
'''
    public int largestSubmatrix(int[][] A) {
        
        int m  = A.length;
        int n = A[0].length;
        
        int[][] sum = new int[m][n];
        
        for(int j = 0; j < n; j++){
            int cnt = 0;
            for(int i = 0; i < m; i++){      
                if(A[i][j] == 0){
                    cnt = 0;
                    sum[i][j] = 0;
                }else{
                    cnt++;
                    sum[i][j] = cnt;
                }
            }
        }
        
        int max = 0;
        for(int i = 0; i < m; i++){
            Arrays.sort(sum[i]);
            for(int j = 0; j < n; j++){
                int a = (n - j)*sum[i][j];
                max = Math.max(a, max);
            }
        }
        return max;
    }
'''

# Intuition
# For each row, find the histogram height of each column.
# Sort it and find the max rectangle you could find(refer to Question 84).


# Complexity
# Time: O(m * n * log(n))
# Space: O(n)

'''
def largestSubmatrix(self, A: List[List[int]]) -> int:
	m, n = len(A), len(A[0])
	H = [0] * n
	ans = 0
	for i in range(m):
		for j in range(n):
			H[j] = H[j] + 1 if A[i][j] else 0
		ans = max(ans, self.getMaxArea(H[:]))
	return ans
    
def getMaxArea(self, heights):
	heights.sort()
	heights.append(-1)
	area = 0
	stack = []
	for i in range(len(heights)):
		while stack and heights[stack[-1]] >= heights[i]:
			h = heights[stack.pop()]
			w = i - stack[-1] - 1 if stack else i
			area = max(area, h * w)
		stack.append(i)
	return area
'''



# YES!!!!! This solution works !!!

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # 1 get prefix sum of each colmun (ruisekiwa)
        # 2 sort by row and use idx to calculate the number of elem and multiply to the value
        # 3 keep track of the max area
        ROW = len(matrix)
        COL = len(matrix[0])
        for col in range(COL):
            cur = 0
            for row in range(ROW):
                if matrix[row][col] == 1:
                    cur += 1
                else:
                    cur = 0       
                matrix[row][col] = cur
        best_area = 0
        for row in range(ROW):
            sortedRow = sorted(matrix[row])
            for col in range(COL):
                area = (COL - col) * sortedRow[col]
                best_area = max(best_area, area)
        return best_area