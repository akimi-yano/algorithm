# 935. Knight Dialer
# Medium

# 631

# 262

# Add to List

# Share
# The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L). The possible movements of chess knight are shown in this diagaram:

# A chess knight can move as indicated in the chess diagram below:


# We have a chess knight and a phone pad as shown below, the knight can only stand on a numeric cell (i.e. blue cell).


# Given an integer n, return how many distinct phone numbers of length n we can dial.

# You are allowed to place the knight on any numeric cell initially and then you should perform n - 1 jumps to dial a number of length n. All jumps should be valid knight jumps.

# As the answer may be very large, return the answer modulo 109 + 7.

 

# Example 1:

# Input: n = 1
# Output: 10
# Explanation: We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.
# Example 2:

# Input: n = 2
# Output: 20
# Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]
# Example 3:

# Input: n = 3
# Output: 46
# Example 4:

# Input: n = 4
# Output: 104
# Example 5:

# Input: n = 3131
# Output: 136006598
# Explanation: Please take care of the mod.
 

# Constraints:

# 1 <= n <= 5000





# This solution works but there might be more efficient solutions !
class Solution:
    mod = 10 ** 9 + 7
    phone = [[1,1,1],[1,1,1],[1,1,1],[0,1,0]]
    moves = ((2,1),(1,2),(2,-1),(1,-2),(-2,1),(-1,2),(-2,-1),(-1,-2))
    def knightDialer(self, n: int) -> int:
        # memo = {}
        @lru_cache(None)
        def helper(row, col, left):
#             if (row,col,left) in memo:
#                 return memo[(row,col,left)]
                
            # if not 0<=row<=3 or not 0<=col<=2 or Solution.phone[row][col] ==0:
            #     return 0
            if left <= 0:
                return 1
            ans = 0
            for r,c in Solution.moves:
                if 0<=row+r<=3 and 0<=col+c<=2 and Solution.phone[row+r][col+c] ==1:
                    ans += helper(row+r,col+c,left-1)
            # memo[(row,col,left)] = ans
            return ans
        
        ans = 0
        for row in range(4):
            for col in range(3):
                if Solution.phone[row][col] == 1:
                    ans += helper(row, col, n-1)
        
        return ans % Solution.mod