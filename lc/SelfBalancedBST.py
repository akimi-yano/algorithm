# 108. Convert Sorted Array to Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#solution1:
# class Solution:
#     def __init__(self):
#         self.root = None
#     def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
#         if len(nums) < 1:
#             return None
#         low = 0
#         high = len(nums)-1
#         mid = (low+high)//2
#         self.root = TreeNode(nums[mid])
#         self.helper(self.root, low, mid-1, nums)
#         self.helper(self.root, mid+1, high, nums)
#         return self.root
        
#     def helper(self, current, low, high, nums):
#         mid = (low+high)//2
#         if low>high:
#             return

#         if nums[mid]>current.val:
#             current.right = TreeNode(nums[mid])
#             self.helper(current.right, low, mid-1, nums)
#             self.helper(current.right, mid+1, high, nums)
#         else:
#             current.left = TreeNode(nums[mid])
#             self.helper(current.left, low, mid-1, nums)
#             self.helper(current.left, mid+1, high, nums)

#solution2:
class Solution:
    def __init__(self):
        self.root = None
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) < 1:
            return None
        low = 0
        high = len(nums)-1
        mid = (low+high)//2
        self.root = TreeNode(nums[mid])
        self.root.left = self.helper(low, mid-1, nums)
        self.root.right = self.helper(mid+1, high, nums)
        return self.root
        
    def helper(self, low, high, nums):
        mid = (low+high)//2
        if low>high:
            return None
        
        current = TreeNode(nums[mid])
        current.left = self.helper(low, mid-1, nums)
        current.right = self.helper(mid+1, high, nums)
        return current
        
