# 1510. Stone Game IV
# Hard

# 553

# 30

# Add to List

# Share
# Alice and Bob take turns playing a game, with Alice starting first.

# Initially, there are n stones in a pile. On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.

# Also, if a player cannot make a move, he/she loses the game.

# Given a positive integer n, return true if and only if Alice wins the game otherwise return false, assuming both players play optimally.

 

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
 

# Constraints:

# 1 <= n <= 105



# This solution works:



class Solution:
    options = [val**2 for val in range(1, int(10**2.5))]

    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(None)
        def helper(remaining, is_Alice):
            if not remaining:
                if is_Alice:
                    return False
                else:
                    return True
                
            if is_Alice:
                for option in Solution.options:
                    if option <= remaining:
                        if helper(remaining-option, False):
                            return True
                    else:
                        break
                return False
            else:
                for option in Solution.options:
                    if option <= remaining:
                        if not helper(remaining-option, True):
                            return False
                    else:
                        break
                return True
                
        return helper(n, True)
            
            
