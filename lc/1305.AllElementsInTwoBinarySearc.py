# 1305. All Elements in Two Binary Search Trees
# Medium

# 547

# 24

# Add to List

# Share
# Given two binary search trees root1 and root2.

# Return a list containing all the integers from both trees sorted in ascending order.


# Example 1:


# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]
# Example 2:

# Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
# Output: [-10,0,0,1,2,5,7,10]
# Example 3:

# Input: root1 = [], root2 = [5,1,7,0,2]
# Output: [0,1,2,5,7]
# Example 4:

# Input: root1 = [0,-10,10], root2 = []
# Output: [-10,0,10]
# Example 5:


# Input: root1 = [1,null,8], root2 = [8,1]
# Output: [1,1,8,8]

# Constraints:

# Each tree has at most 5000 nodes.
# Each node's value is between [-10^5, 10^5].


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# This ACed but there are other ways to do this !
# I initialy thought threre might be a better way, 
# but time and space complecxity wise - its optimal as you cannot do any better than

# Time: O(M+N)
# Space:  O(M+N)

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(cur):
            if not cur:
                return []
            arr = []
            arr.extend(inorder(cur.left))
            arr.append(cur.val)
            arr.extend(inorder(cur.right))
            return arr
        arr1 = inorder(root1)
        arr2 = inorder(root2)
        ans = []
        idx1 = idx2  = 0
        while idx1<len(arr1) and idx2<len(arr2):
            if arr1[idx1]<arr2[idx2]:
                ans.append(arr1[idx1])
                idx1+=1
            else:
                ans.append(arr2[idx2])
                idx2+=1
        while idx1<len(arr1):
            ans.append(arr1[idx1])
            idx1+=1
        while idx2<len(arr2):
            ans.append(arr2[idx2])
            idx2+=1
        return ans