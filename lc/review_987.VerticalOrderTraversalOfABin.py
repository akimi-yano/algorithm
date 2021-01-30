# 987. Vertical Order Traversal of a Binary Tree
# Hard

# 1228

# 2290

# Add to List

# Share
# Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

# For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

# The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

# Return the vertical order traversal of the binary tree.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
# Explanation:
# Column -1: Only node 9 is in this column.
# Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
# Column 1: Only node 20 is in this column.
# Column 2: Only node 7 is in this column.
# Example 2:


# Input: root = [1,2,3,4,5,6,7]
# Output: [[4],[2],[1,5,6],[3],[7]]
# Explanation:
# Column -2: Only node 4 is in this column.
# Column -1: Only node 2 is in this column.
# Column 0: Nodes 1, 5, and 6 are in this column.
#           1 is at the top, so it comes first.
#           5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
# Column 1: Only node 3 is in this column.
# Column 2: Only node 7 is in this column.
# Example 3:


# Input: root = [1,2,3,4,6,5,7]
# Output: [[4],[2],[1,5,6],[3],[7]]
 

# Constraints:

# The number of nodes in the tree is in the range [1, 1000].
# 0 <= Node.val <= 1000

# This solution works:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        arr = []
        def helper(x,y,cur):
            if not cur:
                return 
            arr.append((x,y,cur.val))
            helper(x-1,y+1,cur.left)
            helper(x+1,y+1,cur.right)
        helper(0,0,root)
        arr.sort()
        prev =  float('-inf')
        ans = []
        for elem in arr:
            if prev<elem[0]:
                ans.append([])
                prev=elem[0]
            ans[-1].append(elem[2])           
        return ans

# This solution works:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
import heapq
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        queue = deque([(0,root,0)])
        minheap = []
        while queue:
            newqueue = deque([])
            while queue:
                row, node, col = queue.popleft()
                heapq.heappush(minheap, (col, row, node.val))

                if node.left:
                    newqueue.append((row+1, node.left, col-1))
                if node.right:
                    newqueue.append((row+1, node.right, col+1))
            queue = newqueue
        
        ans = []
        prev = None
        while minheap:
            col, row, value = heapq.heappop(minheap)
            if prev is None or prev < col:
                ans.append([])
            ans[-1].append(value)
            prev = col
        return ans
            
            
            