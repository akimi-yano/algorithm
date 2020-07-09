# 662. Maximum Width of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

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
    
    

#            1        ((1),1)
#          /   \           right and left 1-1+1 = 1
#         3     2     ((3),2) ((2),3)
#        / \     \         left    right            3-2+1 = 2
#       5   3     9   ((5),4) ((3),5)   x  ((9),7)
#                          left                 right 7-4+1 = 4
#
# 
#  A. max_width is 4
# --------------------