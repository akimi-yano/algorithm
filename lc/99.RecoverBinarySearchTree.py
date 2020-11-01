# 99. Recover Binary Search Tree
# Hard

# 1999

# 80

# Add to List

# Share
# You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

# Follow up: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

 

# Example 1:


# Input: root = [1,3,null,null,2]
# Output: [3,1,null,null,2]
# Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
# Example 2:


# Input: root = [3,1,4,null,null,2]
# Output: [2,1,4,null,null,3]
# Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
 

# Constraints:

# The number of nodes in the tree is in the range [2, 1000].
# -231 <= Node.val <= 231 - 1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
#         arr = []
        
#         def helper(cur):
#             if not cur:
#                 return
#             helper(cur.left)
#             arr.append(cur)
#             helper(cur.right)
#         helper(root)
#         prev = arr[0]
#         swap = []
#         for i in range(1, len(arr)):
#             if prev > arr[i]:
#                 swap.append(prev, arr[i])
#                 break
        
        
#         def helper(cur, upper, lower):
#             if not cur:
#                 return None
#             if not lower<cur.val:
#                 cur.left.val, cur.val = cur.val, cur.left.val
                
#             elif not cur.val<upper:
#                 cur.right.val, cur.val = cur.val, cur.right.val
#             else:    
#                 helper(cur.left, cur.val, lower)
#                 helper(cur.right, upper, cur.val)
  
        
#         return helper(root, float('inf'), float('-inf'))


# This solution works !
'''
inorder traversal to append nodes into a list
also make a list of vals that are sorted
compare the sorted arr and node arr 's .val and append them to swap array
swap the values of the swap awway(dont swap nodes or pointers but just vals)

I tried to do it using lower bound and upper bound, but it gets complex by breaking rules at multilpe scopes 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = []
        
        def helper(cur):
            if not cur:
                return
            helper(cur.left)
            arr.append(cur)
            helper(cur.right)
        helper(root)
        
        sorted_val = list(sorted([elem.val for elem in arr]))
        
        swaps = []
        for i in range(len(arr)):
            if sorted_val[i] != arr[i].val:
                swaps.append(arr[i])
        swaps[0].val, swaps[1].val = swaps[1].val, swaps[0].val
            
            
            