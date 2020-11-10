# 1026. Maximum Difference Between Node and Ancestor
# Medium

# 861

# 37

# Add to List

# Share
# Given the root of a binary tree, find the maximum value V for which there exist different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

# A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.

 

# Example 1:


# Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
# Output: 7
# Explanation: We have various ancestor-node differences, some of which are given below :
# |8 - 3| = 5
# |3 - 7| = 4
# |8 - 1| = 7
# |10 - 13| = 3
# Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
# Example 2:


# Input: root = [1,null,2,null,0,3]
# Output: 3
 

# Constraints:

# The number of nodes in the tree is in the range [2, 5000].
# 0 <= Node.val <= 105


# This approach does not work - TLE 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxAncestorDiff(self, root: TreeNode) -> int:
#         def helper(cur):
#             if not cur:
#                 return []
#             if not cur.left and not cur.right:
#                 return [cur]
#             children = []
#             if cur.left:
#                 left = helper(cur.left)
#                 for child in left:
#                     self.max_diff = max(self.max_diff,  abs(child.val-cur.val))
#                     children.extend([cur]+left)
#             if cur.right:
#                 right = helper(cur.right)
#                 for child in right:
#                     self.max_diff = max(self.max_diff,  abs(child.val-cur.val))
#                     children.extend([cur]+right)
            
#             return children
#         self.max_diff = 0
#         helper(root)
#         return self.max_diff


# This solution works !
'''
just kept track of max and min to get max difference!
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def helper(cur, largest, smallest):
            if not cur.left and not cur.right:
                largest = max(largest, cur.val)
                smallest = min(smallest, cur.val)
                max_diff = abs(largest-smallest)
                return max_diff
            
            largest = max(largest, cur.val)
            smallest = min(smallest, cur.val)
            max_diff = abs(largest-smallest)
            if cur.left:
                max_diff = max(max_diff,helper(cur.left, largest, smallest))
            if cur.right:
                max_diff = max(max_diff,helper(cur.right,  largest, smallest))
            return max_diff
        return helper(root, float('-inf'), float('inf'))
        