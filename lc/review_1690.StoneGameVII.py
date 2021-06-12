# 1690. Stone Game VII
# Medium

# 396

# 92

# Add to List

# Share
# Alice and Bob take turns playing a game, with Alice starting first.

# There are n stones arranged in a row. On each player's turn, they can remove either the leftmost stone or the rightmost stone from the row and receive points equal to the sum of the remaining stones' values in the row. The winner is the one with the higher score when there are no stones left to remove.

# Bob found that he will always lose this game (poor Bob, he always loses), so he decided to minimize the score's difference. Alice's goal is to maximize the difference in the score.

# Given an array of integers stones where stones[i] represents the value of the ith stone from the left, return the difference in Alice and Bob's score if they both play optimally.

 

# Example 1:

# Input: stones = [5,3,1,4,2]
# Output: 6
# Explanation: 
# - Alice removes 2 and gets 5 + 3 + 1 + 4 = 13 points. Alice = 13, Bob = 0, stones = [5,3,1,4].
# - Bob removes 5 and gets 3 + 1 + 4 = 8 points. Alice = 13, Bob = 8, stones = [3,1,4].
# - Alice removes 3 and gets 1 + 4 = 5 points. Alice = 18, Bob = 8, stones = [1,4].
# - Bob removes 1 and gets 4 points. Alice = 18, Bob = 12, stones = [4].
# - Alice removes 4 and gets 0 points. Alice = 18, Bob = 12, stones = [].
# The score difference is 18 - 12 = 6.
# Example 2:

# Input: stones = [7,90,5,1,100,10,10,2]
# Output: 122
 

# Constraints:

# n == stones.length
# 2 <= n <= 1000
# 1 <= stones[i] <= 1000

# This solution works:
'''
use total and subtract instead of using prefix sum
also + for alice to gain - for alice to lose (which bob gains)
clear_cache()
'''
 class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        '''
        [5,3,1,4,2]
        0 - 5
        1 - 8
        2 - 9
        3 - 13
        4 - 15
        
        '''
        
        total = sum(stones)
        
        @lru_cache(None)
        def helper(left, right, total, turn):
            if right <= left:
                return 0
            if turn == 0:
                rm_left = helper(left+1, right, total - stones[left], 1) + (total-stones[left])
                rm_right = helper(left, right-1, total - stones[right], 1) + (total-stones[right])
                return max(rm_left, rm_right)
            else:
                rm_left =  (helper(left+1, right, total - stones[left],  0) - (total-stones[left]))
                rm_right = (helper(left, right-1, total - stones[right], 0) - (total-stones[right]))
                return min(rm_left, rm_right)

        ans = helper(0, len(stones)-1, total, 0)
        helper.cache_clear()
        return ans