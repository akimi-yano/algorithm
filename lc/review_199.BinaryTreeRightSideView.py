# 199. Binary Tree Right Side View
# Medium

# 7278

# 400

# Add to List

# Share
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

# Example 1:


# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# Example 2:

# Input: root = [1,null,3]
# Output: [1,3]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100


# This solution works:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        queue = deque([root])
        while queue:
            ans.append(queue[-1].val)
            newqueue = deque([])
            while queue:
                cur = queue.popleft()
                if cur.left:
                    newqueue.append(cur.left)
                if cur.right:
                    newqueue.append(cur.right)
            queue = newqueue
        return ans
        