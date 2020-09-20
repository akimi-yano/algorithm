# 1595. Minimum Cost to Connect Two Groups of Points
# Hard

# 7

# 1

# Add to List

# Share
# You are given two groups of points where the first group has size1 points, the second group has size2 points, and size1 >= size2.

# The cost of the connection between any two points are given in an size1 x size2 matrix where cost[i][j] is the cost of connecting point i of the first group and point j of the second group. The groups are connected if each point in both groups is connected to one or more points in the opposite group. In other words, each point in the first group must be connected to at least one point in the second group, and each point in the second group must be connected to at least one point in the first group.

# Return the minimum cost it takes to connect the two groups.


# Example 1:


# Input: cost = [[15, 96], [36, 2]]
# Output: 17
# Explanation: The optimal way of connecting the groups is:
# 1--A
# 2--B
# This results in a total cost of 17.
# Example 2:


# Input: cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
# Output: 4
# Explanation: The optimal way of connecting the groups is:
# 1--A
# 2--B
# 2--C
# 3--A
# This results in a total cost of 4.
# Note that there are multiple points connected to point 2 in the first group and point A in the second group. This does not matter as there is no limit to the number of points that can be connected. We only care about the minimum total cost.
# Example 3:

# Input: cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
# Output: 10

# Constraints:

# size1 == cost.length
# size2 == cost[i].length
# 1 <= size1, size2 <= 12
# size1 >= size2
# 0 <= cost[i][j] <= 100




# This is the first intuition for the problem - not really a code:
    
# class Solution:
#     def connectTwoGroups(self, cost: List[List[int]]) -> int:
'''
        Input: cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
        Output: 4
        Explanation: The optimal way of connecting the groups is:
        1--A
        2--B
        2--C
        3--A
        
        g1_outer = [0,0,0]
        g2_inner = [0,0,0]
        
        
        1 -> [1,3,5]
        2 -> [4, 1, 1]
        3 -> [1, 5, 3]
        
        A -> [1,4,1]
        B -> [3,1,5]
        C -> [5,1,3]
        
'''
        # def helper()
        


# THIS SOLUTION WORKS!!!:

'''
recursion + memorization
check group1 first (try all) and then check group 2 (assign min if it doesnt have pair)
'''

class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        self.G1 = len(cost)
        self.G2 = len(cost[0])
        self.cost = cost

        g1 = [1 for _ in range(self.G1)]
        g2 = [1 for _ in range(self.G2)]
        self.memo = {}
        return self.helper(tuple(g1), tuple(g2))
    
    def helper(self, g1, g2):
        key = g1, g2
        if key in self.memo:
            return self.memo[key]
        
        ans = float('inf')
        if sum(g1) + sum(g2) < 1:
            ans = 0
        else:
            g1_list = list(g1)
            g2_list = list(g2)
            if sum(g1) > 0:
                g1_list = list(g1)
                g1_idx = g1_list.index(1)
                g1_list[g1_idx] = 0
                for g2_idx in range(self.G2):
                    old_val = g2_list[g2_idx]
                    g2_list[g2_idx] = 0
                    price = self.cost[g1_idx][g2_idx] + self.helper(tuple(g1_list), tuple(g2_list))
                    ans = min(ans, price)
                    g2_list[g2_idx] = old_val
            else:
                total = 0
                for g2_idx in range(self.G2):
                    if g2_list[g2_idx]:
                        best = min([self.cost[_][g2_idx] for _ in range(self.G1)])
                        total += best
                ans = total
        self.memo[key] = ans
        return ans
    

# Optimization ! Using bit mask :

class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        self.G1 = len(cost)
        self.G2 = len(cost[0])
        self.cost = cost

        g1 = g2 = 0
        for _ in range(self.G1):
            g1 = (g1 << 1) + 1
        for _ in range(self.G2):
            g2 = (g2 << 1) + 1
        self.memo = {}
        return self.helper(g1, g2)
    
    def helper(self, g1, g2):
        key = g1, g2
        if key in self.memo:
            return self.memo[key]
        
        ans = float('inf')
        if g1 + g2 < 1:
            ans = 0
        else:
            if g1 > 0:
                g1_idx = 0
                while not g1 & (1 << g1_idx):
                    g1_idx += 1
                for g2_idx in range(self.G2):
                    if g2 & (1 << g2_idx):
                        price = self.cost[g1_idx][g2_idx] \
                        + self.helper(g1 ^ (1 << g1_idx), g2 ^ (1 << g2_idx))
                        ans = min(ans, price)
                    else:
                        price = self.cost[g1_idx][g2_idx] \
                        + self.helper(g1 ^ (1 << g1_idx), g2)
                        ans = min(ans, price)
            else:
                total = 0
                for g2_idx in range(self.G2):
                    if g2 & (1 << g2_idx):
                        best = min([self.cost[_][g2_idx] for _ in range(self.G1)])
                        total += best
                ans = total
        self.memo[key] = ans
        return ans