# 102. Binary Tree Level Order Traversal
# Medium

# 4782

# 107

# Add to List

# Share
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000

# This solution works:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        ans = []
        ans.append([root.val])
        while queue:
            temp = deque([])
            while queue:
                elem = queue.popleft()
                if elem.left:
                    temp.append(elem.left)
                if elem.right:
                    temp.append(elem.right)
            if temp:
                ans.append([node.val for node in temp])
            queue = temp
        return ans
                            