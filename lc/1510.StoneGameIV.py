# 1510. Stone Game IV
# Hard

# 14

# 2

# Add to List

# Share
# Alice and Bob take turns playing a game, with Alice starting first.

# Initially, there are n stones in a pile.  On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.

# Also, if a player cannot make a move, he/she loses the game.

# Given a positive integer n. Return True if and only if Alice wins the game otherwise return False, assuming both players play optimally.

 

# Example 1:

# Input: n = 1
# Output: true
# Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any moves.
# Example 2:

# Input: n = 2
# Output: false
# Explanation: Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -> 1 -> 0).
# Example 3:

# Input: n = 4
# Output: true
# Explanation: n is already a perfect square, Alice can win with one move, removing 4 stones (4 -> 0).
# Example 4:

# Input: n = 7
# Output: false
# Explanation: Alice can't win the game if Bob plays optimally.
# If Alice starts removing 4 stones, Bob will remove 1 stone then Alice should remove only 1 stone and finally Bob removes the last one (7 -> 3 -> 2 -> 1 -> 0). 
# If Alice starts removing 1 stone, Bob will remove 4 stones then Alice only can remove 1 stone and finally Bob removes the last one (7 -> 6 -> 2 -> 1 -> 0).
# Example 5:

# Input: n = 17
# Output: false
# Explanation: Alice can't win the game if Bob plays optimally.
 

# Constraints:

# 1 <= n <= 10^5

# this doesnt work
# import math
# class Solution:
#     def winnerSquareGame(self, n: int) -> bool:
#         def is_square(n):
#             if int(math.sqrt(n))*int(math.sqrt(n)) == n:
#                 return True
#             else:
#                 return False
            
#         # if is_square(n):
#         #     return True
#         # else:
#         #     turn = False
#         turn = True
#         while n>0:
#             for i in range(n,0,-1):
#                 if is_square(i) and n-i>-1:
#                     n-=i
#                     break
#             if n == 0 and turn:
#                 return True
#             elif n == 0 and not turn:
#                 return False
            
#             if turn:
#                 turn = False
#             else:
#                 turn = True
            
#         if n == 0 and turn:
#             return True
#         elif n == 0 and not turn:
#             return False

# this works
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # if I make sure to make the other peson lose then I win
        memo = {}
        def helper(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return False
            p = 1
            while p ** 2 <= n:
                if not helper(n-p**2):
                    memo[n]=True
                    return True
                p += 1
            memo[n]=False
            return False

        return helper(n)