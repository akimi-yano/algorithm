# 662. Maximum Width of Binary Tree
# Medium

# 3736

# 594

# Add to List

# Share
# Given the root of a binary tree, return the maximum width of the given tree.

# The maximum width of a tree is the maximum width among all levels.

# The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes are also counted into the length calculation.

# It is guaranteed that the answer will in the range of 32-bit signed integer.

 

# Example 1:


# Input: root = [1,3,2,5,3,null,9]
# Output: 4
# Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
# Example 2:


# Input: root = [1,3,null,5,3]
# Output: 2
# Explanation: The maximum width existing in the third level with the length 2 (5,3).
# Example 3:


# Input: root = [1,3,2,5]
# Output: 2
# Explanation: The maximum width existing in the second level with the length 2 (3,2).
 

# Constraints:

# The number of nodes in the tree is in the range [1, 3000].
# -100 <= Node.val <= 100


# This solution works:


from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        use index to calcurate and keep track of the width
        '''
        maxwidth = 0
        queue = deque([(root, 1)])
        while queue:
            newqueue = deque([])
            
            _, left = queue[0]
            _, right = queue[-1]
            maxwidth = max(maxwidth, right-left+1)
            
            while queue:
                node, idx = queue.popleft()
                if node.left:
                    newqueue.append((node.left, idx*2))
                if node.right:
                    newqueue.append((node.right, idx*2+1))
            queue = newqueue
        return maxwidth
        