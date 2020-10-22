# 111. Minimum Depth of Binary Tree
# Easy

# 1823

# 759

# Add to List

# Share
# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 2
# Example 2:

# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5
 

# Constraints:

# The number of nodes in the tree is in the range [0, 105].
# -1000 <= Node.val <= 1000


'''
since the definition of leef is not having left or right child, 
we need to find the min level in which the node does not have 
right node or left node
I did BFS using queue to find that, keeping track of the level
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque([(root, 1)])
        
        while queue:
            node, level = queue.popleft()
            if not node.left and not node.right:
                return level
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
