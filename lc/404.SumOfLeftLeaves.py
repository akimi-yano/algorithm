# 404. Sum of Left Leaves

# Find the sum of all left leaves in a given binary tree.

# Example:

#     3
#    / \
#   9  20
#     /  \
#    15   7

# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.



# This solution works ! - there might be a better way though !


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        def helper(cur,is_left):
            if not cur:
                return 0
            
            left_val = helper(cur.left,True)
            right_val = helper(cur.right,False) # right subtree might also have left leaf
            
            total = left_val + right_val 
            
            if is_left and not cur.left and not cur.right: # check if its left and leaf
                total+= cur.val
            
            return total
        
        return helper(root,False) # used bloolean to indicate if its left 
