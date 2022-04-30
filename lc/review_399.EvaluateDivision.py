# 399. Evaluate Division
# Medium

# 4983

# 428

# Add to List

# Share
# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

# Return the answers to all queries. If a single answer cannot be determined, return -1.0.

# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

 

# Example 1:

# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation: 
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
# Example 2:

# Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]
# Example 3:

# Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]
 

# Constraints:

# 1 <= equations.length <= 20
# equations[i].length == 2
# 1 <= Ai.length, Bi.length <= 5
# values.length == equations.length
# 0.0 < values[i] <= 20.0
# 1 <= queries.length <= 20
# queries[i].length == 2
# 1 <= Cj.length, Dj.length <= 5
# Ai, Bi, Cj, Dj consist of lower case English letters and digits.


# This solution works:


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.adj_list = {}
        for i in range(len(equations)):
            e1,e2 = equations[i]
            ans = values[i]
            
            if e1 not in self.adj_list:
                self.adj_list[e1] = []
            self.adj_list[e1].append((e2, ans))
            
            if e2 not in self.adj_list:
                self.adj_list[e2] = []
            
            self.adj_list[e2].append((e1, 1/ans))
            
        res = []
        for q1, q2 in queries:
            res.append(self.helper(q1, q2, set([])))
        return res
            
    def helper(self, cur, target, seen):
        if cur in seen:
            return -1
        seen.add(cur)
        
        if cur not in self.adj_list:
            return -1
        
        if cur == target:
            return 1
    
        for next_node, weight in self.adj_list[cur]:
            temp = weight * self.helper(next_node, target, seen)
            if temp > 0:
                return temp
        
        return -1
            