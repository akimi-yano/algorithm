# 1686. Stone Game VI
# Medium

# 97

# 6

# Add to List

# Share
# Alice and Bob take turns playing a game, with Alice starting first.

# There are n stones in a pile. On each player's turn, they can remove a stone from the pile and receive points based on the stone's value. Alice and Bob may value the stones differently.

# You are given two integer arrays of length n, aliceValues and bobValues. Each aliceValues[i] and bobValues[i] represents how Alice and Bob, respectively, value the ith stone.

# The winner is the person with the most points after all the stones are chosen. If both players have the same amount of points, the game results in a draw. Both players will play optimally.

# Determine the result of the game, and:

# If Alice wins, return 1.
# If Bob wins, return -1.
# If the game results in a draw, return 0.
 

# Example 1:

# Input: aliceValues = [1,3], bobValues = [2,1]
# Output: 1
# Explanation:
# If Alice takes stone 1 (0-indexed) first, Alice will receive 3 points.
# Bob can only choose stone 0, and will only receive 2 points.
# Alice wins.
# Example 2:

# Input: aliceValues = [1,2], bobValues = [3,1]
# Output: 0
# Explanation:
# If Alice takes stone 0, and Bob takes stone 1, they will both have 1 point.
# Draw.
# Example 3:

# Input: aliceValues = [2,4,3], bobValues = [1,6,7]
# Output: -1
# Explanation:
# Regardless of how Alice plays, Bob will be able to have more points than Alice.
# For example, if Alice takes stone 1, Bob can take stone 2, and Alice takes stone 0, Alice will have 6 points to Bob's 7.
# Bob wins.
 

# Constraints:

# n == aliceValues.length == bobValues.length
# 1 <= n <= 105
# 1 <= aliceValues[i], bobValues[i] <= 100



# This approach does not work:

# class Solution:
#     def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
#         if len(aliceValues) == 1:
#             return 1
#         A = {}
#         B = {}
#         for i in range(len(aliceValues)):
#             if aliceValues[i] > bobValues[i]:
#                 A[i] = aliceValues[i] - bobValues[i]
#             elif aliceValues[i] < bobValues[i]:
#                 B[i] = bobValues[i] - aliceValues[i]
        
#         if len(A) > len(B):
#             return 1
#         elif len(B) > len(A):
#             return -1
#         else:
#             # draw or win 
#             if sum(list(A.values())) > sum(list(B.values())):
#                 return 1
#             else:
#                 return 0
            
#             # If Alice wins, return 1.
#             # If Bob wins, return -1.
#             # If the game results in a draw, return 0.
# #         A[2,4,3]
# #         B[1,6,7]
# #           1,2,4
# #           A B B 
        
# #         [1,2], bobValues = 
# #         [3,1]
# #          2, 1
# #          B, A 
        
# #         aliceValues = [1,3], 
# #         bobValues = [2,1]
        
# #         12
# #         BA

# # A = B = {}
# # A[i] = score
# # B[i] = score
# # if len(A) == len(B):
# #     A win or tie - check score
# # elif len(A) > len(B):
# #     A win
# # else:
# #     B win


# This solution works !

class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        '''
        Alice:
        x-a - y-b > y-a - x-b: take X
        
           x-a - y-b > y-a - x_b
        -> x-a + x_b > y-a + y_b
        
        X_total > Y_total: take X
        '''
        pairs = zip(aliceValues, bobValues)
        diff = 0
        for i, (a, b) in enumerate(sorted(pairs, key = lambda tup: -sum(tup))):
            if i % 2 == 0:
                diff += a
            else:
                diff -= b
        if diff > 0:
            return 1
        elif diff < 0:
            return -1
        else:
            return 0
    