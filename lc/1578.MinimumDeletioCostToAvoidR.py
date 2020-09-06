# 1578. Minimum Deletion Cost to Avoid Repeating Letters
# Medium

# 46

# 1

# Add to List

# Share
# Given a string s and an array of integers cost where cost[i] is the cost of deleting the character i in s.

# Return the minimum cost of deletions such that there are no two identical letters next to each other.

# Notice that you will delete the chosen characters at the same time, in other words, after deleting a character, the costs of deleting other characters will not change.

 

# Example 1:

# Input: s = "abaac", cost = [1,2,3,4,5]
# Output: 3
# Explanation: Delete the letter "a" with cost 3 to get "abac" (String without two identical letters next to each other).
# Example 2:

# Input: s = "abc", cost = [1,2,3]
# Output: 0
# Explanation: You don't need to delete any character because there are no identical letters next to each other.
# Example 3:

# Input: s = "aabaa", cost = [1,2,3,4,1]
# Output: 2
# Explanation: Delete the first and the last character, getting the string ("aba").
 

# Constraints:

# s.length == cost.length
# 1 <= s.length, cost.length <= 10^5
# 1 <= cost[i] <= 10^4
# s contains only lowercase English letters.

# THIS SOLUTION WORKS ! 

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        '''
        char: start,end
        
        from start to end: remove from the cheapest ones until its just 1 
        '''
        memo = {}
        prev = None
        prev_idx = -1
        start = 0
        repeated = False
        for i,char in enumerate(s):
            if char != prev:
                if repeated == True:
                    if prev not in memo:
                        memo[prev] = []
                    memo[prev].append((start, prev_idx))
                    repeated = False
                start = i
                
            else:
                repeated = True
            prev_idx = i
            prev = char
        if repeated == True:
            if prev not in memo:
                memo[prev] = []
            memo[prev].append((start, prev_idx))
        total = 0
        for arr in memo.values():
            for v in arr: 
                # print(v)
                start,end =v
                exp = float('-inf')
                for i in range(start,end+1):
                    exp=max(exp,cost[i])
                for i in range(start,end+1):
                    if cost[i] != exp:
                        total+= cost[i]
                    else:
                        exp = float('-inf')
        return total
                