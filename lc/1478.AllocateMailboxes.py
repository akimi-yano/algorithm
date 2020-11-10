# 1478. Allocate Mailboxes
# Hard

# 308

# 4

# Add to List

# Share
# Given the array houses and an integer k. where houses[i] is the location of the ith house along a street, your task is to allocate k mailboxes in the street.

# Return the minimum total distance between each house and its nearest mailbox.

# The answer is guaranteed to fit in a 32-bit signed integer.

 

# Example 1:



# Input: houses = [1,4,8,10,20], k = 3
# Output: 5
# Explanation: Allocate mailboxes in position 3, 9 and 20.
# Minimum total distance from each houses to nearest mailboxes is |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5 
# Example 2:



# Input: houses = [2,3,5,12,18], k = 2
# Output: 9
# Explanation: Allocate mailboxes in position 3 and 14.
# Minimum total distance from each houses to nearest mailboxes is |2-3| + |3-3| + |5-3| + |12-14| + |18-14| = 9.
# Example 3:

# Input: houses = [7,4,6,1], k = 1
# Output: 8
# Example 4:

# Input: houses = [3,6,14,10], k = 4
# Output: 0
 

# Constraints:

# n == houses.length
# 1 <= n <= 100
# 1 <= houses[i] <= 10^4
# 1 <= k <= n
# Array houses contain unique integers.


# This solution works !
'''
DP !
'''

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        self.memo = {}
        self.memo2 = {}
        self.N = len(houses)
        self.houses = houses
        self.houses.sort()

        return self.helper(0, k)
    
    def helper(self, i, remaining):
        key = (i, remaining)
        if key in self.memo:
            return self.memo[key]

        ans = float('inf')
        if i >= self.N:
            ans = 0
        elif remaining < 1:
            pass
        else:
            for j in range(i, self.N-remaining+1):
                ans = min(ans, self.helper(j+1, remaining-1) + self.distance(i, j))

        self.memo[key] = ans
        return ans
    
    def distance(self, start, end):
        key = (start, end)
        if key in self.memo2:
            return self.memo2[key]
        
        m1 = (end + start) // 2
        m2 = (end + start + 1) // 2
        median = (self.houses[m1] + self.houses[m2]) // 2
        ans = sum(abs(median-self.houses[i]) for i in range(start, end+1))
        self.memo2[key] = ans
        return ans
    

# This solution works ! - optimization 
'''
middle index is just (start+end)//2 
'''

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        self.memo = {}
        self.memo2 = {}
        self.N = len(houses)
        self.houses = houses
        self.houses.sort()

        return self.helper(0, k)
    
    def helper(self, i, remaining):
        key = (i, remaining)
        if key in self.memo:
            return self.memo[key]

        ans = float('inf')
        if i >= self.N:
            ans = 0
        elif remaining < 1:
            pass
        else:
            for j in range(i, self.N-remaining+1):
                ans = min(ans, self.helper(j+1, remaining-1) + self.distance(i, j))

        self.memo[key] = ans
        return ans
    
    def distance(self, start, end):
        key = (start, end)
        if key in self.memo2:
            return self.memo2[key]
        middle = self.houses[(start+end)//2]
        ans = sum(abs(middle-self.houses[i]) for i in range(start, end+1))
        self.memo2[key] = ans
        return ans