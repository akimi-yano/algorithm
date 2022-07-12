# 473. Matchsticks to Square
# Medium

# 1942

# 155

# Add to List

# Share
# You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

# Return true if you can make this square and false otherwise.

 

# Example 1:


# Input: matchsticks = [1,1,2,2,2]
# Output: true
# Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
# Example 2:

# Input: matchsticks = [3,3,3,3,4]
# Output: false
# Explanation: You cannot find a way to form a square with all the matchsticks.
 

# Constraints:

# 1 <= matchsticks.length <= 15
# 1 <= matchsticks[i] <= 108


# This solution works:


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False
        total = sum(matchsticks) 
        if total == 0:
            return False
        if total % 4:
            return False
        target = total // 4
        sides = [0 for _ in range(4)]
        matchsticks.sort(reverse = True)
        
        @lru_cache(None)
        def helper(i, sides):
            if i > len(matchsticks)-1:
                for j in range(4):
                    if sides[j] != target:
                        return False
                return True
            for j in range(4):
                new_sides = list(sides)
                if new_sides[j] + matchsticks[i] <= target:
                    new_sides[j] += matchsticks[i]
                    new_sides = tuple(new_sides)
                    if helper(i+1, new_sides):
                        return True
            return False
        return helper(0, tuple(sides))