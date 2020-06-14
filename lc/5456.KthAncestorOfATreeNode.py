# 5456. Kth Ancestor of a Tree Node
# solution1
# Explanation
# A is the parent in 1 step
# Based on this, we can find the parent in 2 steps.
# Again, based on this, we can find the parent in 4 steps.
# And so on.

# This will help you jump fast on the ancestor tree.


# Python:

# class TreeAncestor(object):

#     step = 15
#     def __init__(self, n, A):
#         A = dict(enumerate(A))
#         jump = [A]
#         for s in xrange(self.step):
#             B = {}
#             for i in A:
#                 if A[i] in A:
#                     B[i] = A[A[i]]
#             jump.append(B)
#             A = B
#         self.jump = jump

#     def getKthAncestor(self, x, k):
#         step = self.step
#         while k > 0 and x > -1:
#             if k >= 1 << step:
#                 x = self.jump[step].get(x, -1)
#                 k -= 1 << step
#             else:
#                 step -= 1
#         return x
    
    
# solution2
    
# For node 0, 1, ..., n-1, we define a matrix self.dp[][] whose i, jth element indicates the ith node's 2^j parent. 
# Here, i = 0, 1, ..., n-1 and j = 0, 1, ..., int(log2(n)). An important recursive relationship is that

# self.dp[i][j] = self.dp[self.dp[i][j-1]][j-1].

# In other words, ith node's 2^j parent is ith node's 2^(j-1) parent's 2^(j-1) parent. In this way, 
# lookup is guarenteed to complete in O(logN) time. Note that it takes O(NlogN) to build self.dp.

# Time complexity O(NlogN) to pre-processing the tree and O(logN) for each equery thereafter.

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        m = 1 + int(log2(n)) #at most 16 for this problem 
        self.dp = [[-1] * m for _ in range(n)] #ith node's 2^j parent
        for i in range(n):
            self.dp[i][0] = parent[i] #2^0 parent
            for j in range(1, m):
                if self.dp[i][j-1] != -1: 
                    self.dp[i][j] = self.dp[self.dp[i][j-1]][j-1]
    
    def getKthAncestor(self, node: int, k: int) -> int:
        while k > 0 and node != -1: #sanity check of k is skipped
            i = int(log2(k))
            node = self.dp[node][i]
            k -= (1 << i)
        return node 