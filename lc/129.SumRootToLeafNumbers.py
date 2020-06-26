# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/542/week-4-june-22nd-june-28th/3372/
# 129. Sum Root to Leaf Numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# attempt 1

# input [1,2,3]
#    1
#   / \
#  2   3
# self.total  0
# helper((1),"")
# cur (1)
# val "1"

# helper((2),"1")
#     val "12"
#     helper((none),'12') 
#         self.total 12
#     helper((none),'12')
#         self.total 12



# helper((3),"1")
#     val '13'
#     helper((none),'13')
#         self.total 13
#     helper((none),'13')
#         self.total 13

 # soooo it does not work because you are adding the number twice       
# class Solution:
#     def sumNumbers(self, root: TreeNode) -> int:
#         self.total = 0
#         def helper(cur, val):
#             # print(val)
#             if cur is None:
#                 self.total+=int(val)
#                 return 
#             val+=str(cur.val)
#             helper(cur.left,val)
#             helper(cur.right,val)        
#         helper(root,"")
#         return self.total
    
    
# attempt 2
    
# input [1,2,3]
#    1
#   / \
#  2   3
# total = 0

# helper((1),"")
# cur (1)
# val "1"
# helper(2,"1")

# helper(3,"1")

    
    
# THIS DIDNT WORK becasue it didnt handle edge case of root being None and 
# also I needed to add the value of the current node before adding it up to the total sum
# class Solution:
#     def sumNumbers(self, root: TreeNode) -> int:
        
#         self.total = 0
#         def helper(cur, val):
#             # print(val)
#             val+=str(cur.val)
#             if cur.left is None and cur.right is None:
#                 self.total+=int(val)
#                 return 
#             if cur.left is not None:
#                 helper(cur.left,val)
#             if cur.right is not None:
#                 helper(cur.right,val)        
#         helper(root,"")
#         return self.total
    
    
# attempt 3

# THIS WORKS!!!!
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.total = 0
        def helper(cur, val):
            val+=str(cur.val)
            if cur.left is None and cur.right is None:
                self.total+=int(val)
                return 
            if cur.left is not None:
                helper(cur.left,val)
            if cur.right is not None:
                helper(cur.right,val)        
        helper(root,"")
        return self.total