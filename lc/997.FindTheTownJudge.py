# 997. Find the Town Judge
# Easy

# 2513

# 179

# Add to List

# Share
# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

# Example 1:

# Input: n = 2, trust = [[1,2]]
# Output: 2
# Example 2:

# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3
# Example 3:

# Input: n = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1
 

# Constraints:

# 1 <= n <= 1000
# 0 <= trust.length <= 104
# trust[i].length == 2
# All the pairs of trust are unique.
# ai != bi
# 1 <= ai, bi <= n


# This solution works:


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        '''
        0 trusts 1
        1) The town judge trusts nobody.
        2) Everybody (except for the town judge) trusts the town judge.
        '''
        if not trust:
            return 1 if n == 1 else -1
        
        adj = {}
        reverse_adj = {}
        for a, b in trust:
            if a not in adj:
                adj[a] = []
            adj[a].append(b)
            
            if b not in reverse_adj:
                reverse_adj[b] = []
            reverse_adj[b].append(a)
        
        maybe_judges = []
        for person in range(1, n+1):
            if person not in adj:
                maybe_judges.append(person)
        
        for cand in maybe_judges:
            if cand in reverse_adj:
                # check the length of the arr as all the pairs of trust are unique
                if len(reverse_adj[cand]) == n-1:
                    return cand
        return -1 
                    
                    
        