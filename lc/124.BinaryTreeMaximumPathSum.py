# 124. Binary Tree Maximum Path Sum
# Hard

# 4655

# 337

# Add to List

# Share
# Given a non-empty binary tree, find the maximum path sum.

# For this problem, a path is defined as any node sequence from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

 

# Example 1:


# Input: root = [1,2,3]
# Output: 6
# Example 2:


# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
 

# Constraints:

# The number of nodes in the tree is in the range [0, 3 * 104].
# -1000 <= Node.val <= 1000

# This approach does not work 

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def maxPathSum(self, root: TreeNode) -> int:
#         def helper(cur):
#             if not cur:
#                 return float('-inf')
#             left = helper(cur.left)
#             right = helper(cur.right)
#             return max(left, left+cur.val, right, right+cur.val, left+right+cur.val, cur.val)
#         return helper(root)



# This approach works !

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def helper(cur):
            if not cur:
                return 0
            left = max(helper(cur.left),0)
            right = max(helper(cur.right),0)
            third = left + right + cur.val
            
            self.total = max(self.total, third)
            return max(left, right) + cur.val
        
        self.total = float('-inf')
        helper(root)
        return self.total


'''
Good explanation:
https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram


1. class Solution:
2.     def maxPathSum(self, root: TreeNode) -> int:
3. 		max_path = float("-inf") # placeholder to be updated
4. 		def get_max_gain(node):
5. 			nonlocal max_path # This tells that max_path is not a local variable
6. 			if node is None:
7. 				return 0
8. 				
9. 			gain_on_left = max(get_max_gain(node.left), 0) # Read the part important observations
10. 		gain_on_right = max(get_max_gain(node.right), 0)  # Read the part important observations
11. 			
12. 		current_max_path = node.val + gain_on_left + gain_on_right # Read first three images of going down the recursion stack
13. 		max_path = max(max_path, current_max_path) # Read first three images of going down the recursion stack
14. 			
15. 		return node.val + max(gain_on_left, gain_on_right) # Read the last image of going down the recursion stack
16. 			
17. 			
18. 	get_max_gain(root) # Starts the recursion chain
19. 	return max_path		
'''

