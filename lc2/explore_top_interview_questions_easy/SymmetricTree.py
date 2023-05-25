'''
101. Symmetric Tree
Easy
13.5K
302
Companies
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 

Follow up: Could you solve it both recursively and iteratively?
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(cur1, cur2):
            if not cur1 and not cur2:
                return True
            elif not cur1 or not cur2:
                return False
            return cur1.val == cur2.val and helper(cur1.left, cur2.right) and helper(cur1.right, cur2.left)
        return helper(root.left, root.right)