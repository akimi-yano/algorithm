# 1916. Count Ways to Build Rooms in an Ant Colony
# Hard

# 145

# 22

# Add to List

# Share
# You are an ant tasked with adding n new rooms numbered 0 to n-1 to your colony. You are given the expansion plan as a 0-indexed integer array of length n, prevRoom, where prevRoom[i] indicates that you must build room prevRoom[i] before building room i, and these two rooms must be connected directly. Room 0 is already built, so prevRoom[0] = -1. The expansion plan is given such that once all the rooms are built, every room will be reachable from room 0.

# You can only build one room at a time, and you can travel freely between rooms you have already built only if they are connected. You can choose to build any room as long as its previous room is already built.

# Return the number of different orders you can build all the rooms in. Since the answer may be large, return it modulo 109 + 7.

 

# Example 1:


# Input: prevRoom = [-1,0,1]
# Output: 1
# Explanation: There is only one way to build the additional rooms: 0 → 1 → 2
# Example 2:


# Input: prevRoom = [-1,0,0,1,2]
# Output: 6
# Explanation:
# The 6 ways are:
# 0 → 1 → 3 → 2 → 4
# 0 → 2 → 4 → 1 → 3
# 0 → 1 → 2 → 3 → 4
# 0 → 1 → 2 → 4 → 3
# 0 → 2 → 1 → 3 → 4
# 0 → 2 → 1 → 4 → 3
 

# Constraints:

# n == prevRoom.length
# 2 <= n <= 105
# prevRoom[0] == -1
# 0 <= prevRoom[i] < n for all 1 <= i < n
# Every room is reachable from room 0 once all the rooms are built.

# This solution works:

mod=10**9+ 7
class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        N=len(prevRoom)
        Adj=[[] for _ in range(N)]
        Indegree=[0]*N
        Fac=[1]*(N+1)
        Inv=[1]*(N+1)
        for n in range(1,N+1):
            Fac[n]=n*Fac[n-1]%mod
            Inv[n]=pow(Fac[n],mod-2,mod)
        
        for i in range(1,len(prevRoom)):
            Adj[prevRoom[i]].append(i)
        
        children=[0]*N
        
        def findChildren(node):
            nonlocal children
            ans=1
            for child in Adj[node]:
                ans+=findChildren(child)
            
            children[node]=ans
            return ans
        
        findChildren(0)
        
        def find(node):
            val=1
            for child in Adj[node]:
                val*=find(child)
                val%=mod
                
            total=0
            childcnt=[]
            for child in Adj[node]:
                total+=children[child]
                childcnt.append(children[child])
            
            
            val*=Fac[total]
            val%=mod
            
            for cnt in childcnt:
                val*=Inv[cnt]
                val%=mod
            return val
        
        return find(0)
    
    
    """
    The following problem is solved using DP+Recursion+Euler theorem to find Inverse +keeping of children+combinotrics.

    One key challenge is also get the idea to interleave the topological sorts of the all the childrens which is done by combinotrics.
    """
