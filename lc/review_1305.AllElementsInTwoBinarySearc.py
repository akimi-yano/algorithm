# 1305. All Elements in Two Binary Search Trees
# Medium

# 1419

# 48

# Add to List

# Share
# Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

 

# Example 1:


# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]
# Example 2:


# Input: root1 = [1,null,8], root2 = [8,1]
# Output: [1,1,8,8]
 

# Constraints:

# The number of nodes in each tree is in the range [0, 5000].
# -105 <= Node.val <= 105


# This solution works:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def helper(cur):
            nonlocal arr
            if not cur:
                return 
            helper(cur.left)
            arr.append(cur.val)
            helper(cur.right)
            
        arr = []
        helper(root1)
        arr1 = list(arr)
        
        arr = []
        helper(root2)
        arr2 = list(arr)
        
        ans = []
        idx1 = idx2 = 0
        while idx1 < len(arr1) and idx2 < len(arr2):
            if arr1[idx1] < arr2[idx2]:
                ans.append(arr1[idx1])
                idx1 += 1
            else:
                ans.append(arr2[idx2])
                idx2 += 1
        
        while idx1 < len(arr1):
                ans.append(arr1[idx1])
                idx1 += 1
        
        while idx2 < len(arr2):
                ans.append(arr2[idx2])
                idx2 += 1
        
        return ans