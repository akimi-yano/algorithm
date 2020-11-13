'''
Input: A = [1,4,2], B = [1,2,4]
Output: 2
Explanation: We ti can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.
Example 2:

Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
Output: 3
Example 3:

Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
Output: 2
'''


def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # m, n = len(text1),len(text2)
        # dp = [ [0]*(n+1) for i in range(m+1)]
        # # fill out the 2D table
        # for i in range(m):
        #     for j in range(n):
        #         if text1[i]==text2[j]:
        #             dp[i+1][j+1]=dp[i][j]+1
        #         else:
        #             dp[i+1][j+1]= max(dp[i+1][j],dp[i][j+1])
        # return int(dp[m][n])
        
        if not text1 or not text2: return None
        
        col_size = len(text1)
        size = len(text2)
        
        dp = [[0 for _ in range(col_size+1)] for _ in range(size+1)]
        
        for i in range(size):
            for j in range(col_size):
                if text2[i] == text1[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
                    
        return dp[-1][-1]

# A  [1 4 2]

# count = 2

# B  [1 2 4]

# |\
