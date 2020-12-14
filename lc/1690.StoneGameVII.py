# 1690. Stone Game VII
# Medium

# 45

# 43

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

# This approach does not work :   - need to do dp for both Alice's and Bob's
# from collections import deque
# class Solution:
#     def stoneGameVII(self, stones: List[int]) -> int:
#         queue = deque(stones)
#         total = sum(stones)
#         # print(total)
#         # self.A = 0
#         return self.minimize_diff(queue, total)
        
    
#     def minimize_diff(self, queue, total):
#         if len(queue) <= 1:
#             return 0
#         # self.A += self.maximize_diff(queue, total)    
#         left = queue[0]
#         right = queue[-1]
#         if left < right:
#             point = queue.popleft()
#         else:
#             point = queue.pop()    
#         total -= point
#         A = total
       
#         min_diff = float('inf')
#         if queue:
#             min_diff = min(min_diff, A - (total-queue[0] + self.minimize_diff(deque(list(queue)[1:]), total-queue[0])))
#         if queue:
#             min_diff = min(min_diff, A - (total-queue[-1] + self.minimize_diff(deque(list(queue)[:-1]), total-queue[-1])))
        
#         return min_diff
        
#     def maximize_diff(self, queue, total):
#         if len(queue) <= 1:
#             point = queue.pop()
#         else:
#             left = queue[0]
#             right = queue[-1]
#             if left < right:
#                 point = queue.popleft()
#             else:
#                 point = queue.pop()
                
#         total -= point
#         return total


# This approach does not work - TLE :

# class Solution:
#     def stoneGameVII(self, stones: List[int]) -> int:
#         self.stones = stones
#         return self.helper(0, len(stones)-1,sum(stones), True)
    
#     @lru_cache(None)
#     def helper(self, left, right, total, aturn):
#         if left >= right:
#             return 0   
#         left_stone = self.stones[left]
#         right_stone = self.stones[right]
#         if aturn:
#             # if it's alice's turn, add the subarray sum to the diff
#             diff1 = self.helper(left+1, right, total - left_stone, False) + total - left_stone
#             diff2 = self.helper(left, right-1, total - right_stone, False) + total - right_stone
#         else:
#             # if it's bob's turn, subtract the subarray sum (because bob getting points means alice is losing points)
#             diff1 = self.helper(left+1, right, total - left_stone, True) - total + left_stone
#             diff2 = self.helper(left, right-1, total - right_stone, True) - total + right_stone
#         if aturn:
#             return max(diff1, diff2)
#         else:
#             return min(diff1, diff2)


# This solution works !:
'''
This magic 1 line let me pass all the test cases !!!: 

self.helper.cache_clear()

It clears the cache after every call :)

'''

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        self.stones = stones
        
        ans = self.helper(0, len(stones)-1,sum(stones), True)
        self.helper.cache_clear()
        return ans
    
    @lru_cache(None)
    def helper(self, left, right, total, aturn):
        if left >= right:
            return 0   
        left_stone = self.stones[left]
        right_stone = self.stones[right]
        if aturn:
            # if it's alice's turn, add the subarray sum to the diff
            diff1 = self.helper(left+1, right, total - left_stone, False) + total - left_stone
            diff2 = self.helper(left, right-1, total - right_stone, False) + total - right_stone
        else:
            # if it's bob's turn, subtract the subarray sum (because bob getting points means alice is losing points)
            diff1 = self.helper(left+1, right, total - left_stone, True) - total + left_stone
            diff2 = self.helper(left, right-1, total - right_stone, True) - total + right_stone
        if aturn:
            return max(diff1, diff2)
        else:
            return min(diff1, diff2)

