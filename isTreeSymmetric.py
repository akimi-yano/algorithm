# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 101. Symmetric Tree
# Easy
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

class Solution:
        
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.traverse(root.left, root.right)
        
    def traverse(self, left, right):
        if left is None or right is None:
            return left is None and right is None
        return left.val == right.val and self.traverse(left.left, right.right) and self.traverse(left.right, right.left)
   

# the solution below did not work for cases where there are null and structure is not even
# class Solution:
    # def __init__(self):
    #     self.leftArr=[]
    #     self.rightArr=[]
        
    # def isSymmetric(self, root: TreeNode) -> bool:
 #        if root is None:
 #            return True
        # print(self.leftInorder(root.left,self.leftArr))
        # print(self.rightReverseInorder(root.right,self.rightArr))
        # if len(self.leftArr)!= len(self.rightArr):
        #     return False
        # for i in range(len(self.leftArr)):
        #     if self.leftArr[i]!=self.rightArr[i]:
        #         return False
        # return True
#     def leftInorder(self, current, arr):
#         if current is None:
#             return self.leftArr
#         self.leftInorder(current.left,arr)
#         self.leftArr.append(current.val)
#         self.leftInorder(current.right,arr)
#         return self.leftArr
            
#     def rightReverseInorder(self, current, arr):
#         if current is None:
#             return self.rightArr
#         self.rightReverseInorder(current.right,arr)
#         self.rightArr.append(current.val)
#         self.rightReverseInorder(current.left,arr)
#         return self.rightArr
        
