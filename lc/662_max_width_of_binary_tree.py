# 662. Maximum Width of Binary Tree
# Medium

# 1465

# 291

# Add to List

# Share
# Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

# The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

# Example 1:

# Input: 

#            1
#          /   \
#         3     2
#        / \     \  
#       5   3     9 

# Output: 4
# Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
# Example 2:

# Input: 

#           1
#          /  
#         3    
#        / \       
#       5   3     

# Output: 2
# Explanation: The maximum width existing in the third level with the length 2 (5,3).
# Example 3:

# Input: 

#           1
#          / \
#         3   2 
#        /        
#       5      

# Output: 2
# Explanation: The maximum width existing in the second level with the length 2 (3,2).
# Example 4:

# Input: 

#           1
#          / \
#         3   2
#        /     \  
#       5       9 
#      /         \
#     6           7
# Output: 8
# Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


# Note: Answer will in the range of 32-bit signed integer.




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# yay this works

from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        queue = deque([(root,1)])
        max_width = 0
        while len(queue)>0:
            _,left = queue[0]
            _,right = queue[-1]
            max_width = max(max_width,right-left+1)
            next_level = deque([])
            while len(queue)>0:
                node,index = queue.popleft()
                if node.left: 
                    next_level.append((node.left,index*2))
                if node.right:
                    next_level.append((node.right,index*2+1))
            queue = next_level
        return max_width
    
    
    
    # did this again myself and it works !!!!!!
    
    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: 
            return 0
        queue = deque([(root,1)])
        max_width = 0
        while len(queue)>0:
            temp = deque([])
            _,left = queue[0]
            _,right = queue[-1]
            max_width = max(max_width, right-left+1)
            
            while len(queue)>0:
                node, idx = queue.popleft()
                if node.left:
                    temp.append((node.left,idx*2))
                if node.right:
                    temp.append((node.right,idx*2+1))
            queue = temp
            
        return max_width