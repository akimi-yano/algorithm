# 814. Binary Tree Pruning
# Medium

# 1146

# 44

# Add to List

# Share
# We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

# Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

# (Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

# Example 1:
# Input: [1,null,0,0,1]
# Output: [1,null,0,null,1]
 
# Explanation: 
# Only the red nodes satisfy the property "every subtree not containing a 1".
# The diagram on the right represents the answer.


# Example 2:
# Input: [1,0,1,0,0,0,1]
# Output: [1,null,1,null,1]



# Example 3:
# Input: [1,1,0,1,1,0,1,0]
# Output: [1,1,0,1,1,null,1]



# Note:

# The binary tree will have at most 200 nodes.
# The value of each node will only be 0 or 1.




# This approach does not work :
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def pruneTree(self, root: TreeNode) -> TreeNode:
#         '''
#         recursively traverse the tree
#         each tree returns True / False 
#         if the left child does not have 1 -> reassign it to None 
        
#         '''
#         def helper(cur):
#             if not cur:
#                 return 0
#             ans = 0
#             ans += cur.val
                
#             left = helper(cur.left) 
#             if left is not None and left == 0:
#                 cur.left = None
#             right = helper(cur.right)
#             if right is not None and right == 0:
#                 cur.right = None
#             return ans 
        
#         return helper(root)



# This solution works :

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        '''
        recursively traverse the tree
        each tree returns True / False 
        if the left child does not have 1 -> reassign it to None 
        
        IMPORTANT: 
        1 return root if helper return interger > 0 else return None
        2 even if yourself is 0, if your left child or right child is 1, we can keep the subtree so we need to add left and right to your self before returning it
        
        '''
        def helper(cur):
            if not cur:
                return 0

            left = helper(cur.left) 
            if left == 0:
                cur.left = None
                
            right = helper(cur.right)
            if right == 0:
                cur.right = None
                
            return cur.val + left + right
        
        return root if helper(root) > 0 else None