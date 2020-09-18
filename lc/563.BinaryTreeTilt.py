# 563. Binary Tree Tilt
# Easy

# 565

# 1379

# Add to List

# Share
# Given a binary tree, return the tilt of the whole tree.

# The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.

# The tilt of the whole tree is defined as the sum of all nodes' tilt.

# Example:
# Input: 
#          1
#        /   \
#       2     3
# Output: 1
# Explanation: 
# Tilt of node 2 : 0
# Tilt of node 3 : 0
# Tilt of node 1 : |2-3| = 1
# Tilt of binary tree : 0 + 0 + 1 = 1
# Note:

# The sum of node values in any subtree won't exceed the range of 32-bit integer.
# All the tilt values won't exceed the range of 32-bit integer.


# THIS APPROACH DOES NOT WORK 

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def findTilt(self, root: TreeNode) -> int:
#         # def helper(cur):
#         #     if  not cur:
#         #         return 
#         #     cur.left = helper(cur.left)
#         #     cur.right = helper(cur.right)
#         #     return cur
#         # return helper(root)
#         self.count  = 0
#         def helper(cur):
#             if not cur:
#                 return None
#             if cur.left and cur.right:
#                 cur.left = helper(cur.left)
#                 cur.right  = helper(cur.right)
#                 tilt  = abs(cur.left.val  - cur.right.val)
#                 self.count += tilt
#             elif cur.left:
#                 cur.left = helper(cur.left)
#                 tilt = abs(cur.left.val-0)
#                 self.count += tilt  
#             elif cur.right:
#                 cur.right = helper(cur.right)
#                 tilt = abs(0-cur.right.val)
#                 self.count += tilt
#             else:
#                 tilt = abs(0-0)
#                 self.count += tilt
#             return cur
#         helper(root)
#         return self.count
#         '''
#          1
#         /\
#        2  3
    
    
#     2 - 0
#     3 - 0
#     1 - 1
#     whole tree :1 
    
#     tilt = abs diff bw 
#         sum of left sub tree node val and 
#         sum of right sub tree node val
#     tilt of who tree  =  sum all nodes tilt
    
#      1
#     /\
#    2  3
#   /   /
# 4    5

# 1 -  (6-8) = 2  
# 2 - 4
# 3   - 5
# 4  - 0
# 5 - 0


#        '''


# THIS SOLUTION WORKS !:

'''
I need to keep track of the sum and tilt (I do that by using tuple)
I dont need to return cur or assign it to cur.left and cur.right because I am not modifying the nodes here 

STEPS:
1 write a code to culculate the sum
2 write a code to culculate the tilt 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def helper(cur):
            if not cur:
                return 0, 0
            left_total, left_tilt = helper(cur.left) 
            right_total, right_tilt = helper(cur.right)
            total = left_total + right_total + cur.val
            tilt = abs(left_total-right_total) + left_tilt + right_tilt
            return total, tilt
            
        return helper(root)[1]
   
        '''
         1
        /\
       2  3
    
    
    2 - 0
    3 - 0
    1 - 1
    whole tree :1 
    
    tilt = abs diff bw 
        sum of left sub tree node val and 
        sum of right sub tree node val
    tilt of who tree  =  sum all nodes tilt
    
     1
    /\
   2  3
  /   /
4    5

1 -  (6-8) = 2  
2 - 4
3   - 5
4  - 0
5 - 0
       
       '''
        