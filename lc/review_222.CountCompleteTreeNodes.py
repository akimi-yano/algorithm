# 222. Count Complete Tree Nodes
# Medium

# 3681

# 284

# Add to List

# Share
# Given the root of a complete binary tree, return the number of the nodes in the tree.

# According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Design an algorithm that runs in less than O(n) time complexity.

 

# Example 1:


# Input: root = [1,2,3,4,5,6]
# Output: 6
# Example 2:

# Input: root = []
# Output: 0
# Example 3:

# Input: root = [1]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5 * 104].
# 0 <= Node.val <= 5 * 104
# The tree is guaranteed to be complete.


# This solution works:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        '''
               1
             2   3
            4 5
        '''
        def helper(count):
            nonlocal root
            cur = count
            directions = []
            while cur > 1:
                if cur % 2 == 1:
                    directions.append('r')
                else:
                    directions.append('l')
                cur //= 2
            
            curnode = root
            while len(directions) > 0:
                d = directions.pop()
                if d == 'l':
                    curnode = curnode.left
                else:
                    curnode = curnode.right
            return curnode is not None
                
        
        if not root:
            return 0
        
        left = 1
        node = root
        while node.left is not None:
            left *= 2
            node = node.left
        right = left * 2 - 1
        while left < right:
            mid = (left + right + 1) // 2
            if helper(mid):
                left = mid
            else:
                right = mid - 1
        return left
