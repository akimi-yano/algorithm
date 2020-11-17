# 1659. Maximize Grid Happiness
# Hard

# 54

# 26

# Add to List

# Share
# You are given four integers, m, n, introvertsCount, and extrovertsCount. You have an m x n grid, and there are two types of people: introverts and extroverts. There are introvertsCount introverts and extrovertsCount extroverts.

# You should decide how many people you want to live in the grid and assign each of them one grid cell. Note that you do not have to have all the people living in the grid.

# The happiness of each person is calculated as follows:

# Introverts start with 120 happiness and lose 30 happiness for each neighbor (introvert or extrovert).
# Extroverts start with 40 happiness and gain 20 happiness for each neighbor (introvert or extrovert).
# Neighbors live in the directly adjacent cells north, east, south, and west of a person's cell.

# The grid happiness is the sum of each person's happiness. Return the maximum possible grid happiness.


# Example 1:


# Input: m = 2, n = 3, introvertsCount = 1, extrovertsCount = 2
# Output: 240
# Explanation: Assume the grid is 1-indexed with coordinates (row, column).
# We can put the introvert in cell (1,1) and put the extroverts in cells (1,3) and (2,3).
# - Introvert at (1,1) happiness: 120 (starting happiness) - (0 * 30) (0 neighbors) = 120
# - Extrovert at (1,3) happiness: 40 (starting happiness) + (1 * 20) (1 neighbor) = 60
# - Extrovert at (2,3) happiness: 40 (starting happiness) + (1 * 20) (1 neighbor) = 60
# The grid happiness is 120 + 60 + 60 = 240.
# The above figure shows the grid in this example with each person's happiness. The introvert stays in the light green cell while the extroverts live on the light purple cells.
# Example 2:

# Input: m = 3, n = 1, introvertsCount = 2, extrovertsCount = 1
# Output: 260
# Explanation: Place the two introverts in (1,1) and (3,1) and the extrovert at (2,1).
# - Introvert at (1,1) happiness: 120 (starting happiness) - (1 * 30) (1 neighbor) = 90
# - Extrovert at (2,1) happiness: 40 (starting happiness) + (2 * 20) (2 neighbors) = 80
# - Introvert at (3,1) happiness: 120 (starting happiness) - (1 * 30) (1 neighbor) = 90
# The grid happiness is 90 + 80 + 90 = 260.
# Example 3:

# Input: m = 2, n = 2, introvertsCount = 4, extrovertsCount = 0
# Output: 240

# Constraints:

# 1 <= m, n <= 5
# 0 <= introvertsCount, extrovertsCount <= min(m * n, 6)



# This approach does not work :
# class Solution:
#     def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
#         ROW = m
#         COL = n
#         grid = [[0 for _ in range(COL)] for _ in range(ROW)]
        
#         def helper(intro, extro, grid):
#             if intro:
                
#                 helper(intro-1, extro, grid)
#             if extro:
#                 helper(intro, extro-1,  grid)


# This solution works !
'''
DP: 3 options
1 dont place anyone 
2 place introvert person
3 place extrovert person
'''
class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        def getHappiness(j, type, lastValues):
            up = lastValues[j]
            left = lastValues[j-1] if j > 0 else ""
            
            up_diff = 0
            if up == "i":
                up_diff = -30
            elif up == "e":
                up_diff = 20
                
            left_diff = 0
            if left == "i":
                left_diff = -30
            elif left == "e": 
                left_diff = 20
            
            neighbors = (1 if up else 0) + (1 if left else 0)
            
            ans = 0
            if type == "i":
                ans = 120 - 30 *neighbors + left_diff + up_diff
            elif type == "e":
                ans = 40 + 20 * neighbors + left_diff + up_diff
            return ans
        # starting from pos to the end of the grid, the max happiness we can get
        @lru_cache(None)
        def dp(pos, intro, extro, lastValues):
            if pos == m * n:
                return 0
            j = pos % n
            ans = 0
            list_lastValues = list(lastValues)
            old_value = list_lastValues[j]
            
            # not place any person
            list_lastValues[j] = ""
            ans = dp(pos+1, intro, extro, tuple(list_lastValues))
            list_lastValues[j] = old_value
            
            # place an introvert person
            if intro: 
                happiness = getHappiness(j, "i", lastValues)
                list_lastValues[j] = "i"
                ans = max(ans, happiness + dp(pos+1, intro-1, extro, tuple(list_lastValues)))
                list_lastValues[j] = old_value
            
            # place an extrovert person
            if extro:
                happiness = getHappiness(j, "e", lastValues)
                list_lastValues[j] = "e"
                ans = max(ans, happiness + dp(pos+1, intro, extro-1, tuple(list_lastValues)))
                list_lastValues[j] = old_value
            
            return ans
        return dp(0, introvertsCount, extrovertsCount, tuple([""]*n))
            
            