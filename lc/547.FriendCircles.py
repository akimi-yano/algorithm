# 547. Friend Circles
# Medium

# 2170

# 151

# Add to List

# Share
# There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

# Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

# Example 1:

# Input: 
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# Output: 2
# Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
# The 2nd student himself is in a friend circle. So return 2.
 

# Example 2:

# Input: 
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# Output: 1
# Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
# so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.

 

# Constraints:

# 1 <= N <= 200
# M[i][i] == 1
# M[i][j] == M[j][i]



# THIS SOLUTION WORKS  !!! - UNION FIND approach  :)

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        '''
        self edge for all and start connecting all
        
        union find for all to see if all are unique
            j j j
        i [[1,1,0],
        i  [1,1,0],
        i  [0,0,1]]
        0 - N-1 students
        no direction
        0 - 0,1 -> [1]
        1 - 0,1 -> [0]
        2 - 2 -> []
        0,1,2
        [0, 0, 2]
[[1,1,0],
 [1,1,1],
 [0,1,1]]
 
 [[1,0,0,1],
  [0,1,1,0],
  [0,1,1,1],
  [1,0,1,1]]
 0 - 3
 1 - 2
 2 - 3
 
        '''
        N = len(M)
        # start with self edge
        self.roots = [i for i in range(N)]
        
        # only traverse the upper half to eliminate redundency 
        for row in range(N):
            for col in range(row+1, N):
                if M[row][col] == 1 and row != col:
                    self.union(row, col)
                    
        # call find again to connect the indirect relationships
        for i in range(len(self.roots)):
            self.find(i)
            
        # return the unique number of circles
        return len(set(self.roots))
                    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        # always set it to smaller number to easily find the circle later
        if x != y:
            self.roots[max(x,y)] = min(x,y)
            
    def find(self, x):
        if x == self.roots[x]:
            return x
        self.roots[x] = self.find(self.roots[x])
        return self.roots[x]
        
        
        
# Another solution 
'''
From some source, we can visit every connected node to it with a simple DFS. 
As is the case with DFS's, seen will keep track of nodes that have been visited.

For every node, we can visit every node connected to it with this DFS, 
and increment our answer as that represents one friend circle (connected component.)
'''
def findCircleNum(self, A):
    N = len(A)
    seen = set()
    def dfs(node):
        for nei, adj in enumerate(A[node]):
            if adj and nei not in seen:
                seen.add(nei)
                dfs(nei)
    
    ans = 0
    for i in range(N):
        if i not in seen:
            dfs(i)
            ans += 1
    return ans