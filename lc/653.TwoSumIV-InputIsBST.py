# 653. Two Sum IV - Input is a BST
# Easy

# 1638

# 144

# Add to List

# Share
# Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.



# Example 1:


# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true
# Example 2:


# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false
# Example 3:

# Input: root = [2,1,3], k = 4
# Output: true
# Example 4:

# Input: root = [2,1,3], k = 1
# Output: false
# Example 5:

# Input: root = [2,1,3], k = 3
# Output: true


# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -104 <= Node.val <= 104
# root is guaranteed to be a valid binary search tree.
# -105 <= k <= 105



# This solution does not work 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def findTarget(self, root: TreeNode, k: int) -> bool:
#         to_find = {}
#         def helper(cur):
#             if not cur:
#                 return
#             if k-cur.val not in to_find:
#                 to_find[k-cur.val] = 1
#             to_find[k-cur.val] +=1
#             helper(cur.left)
#             helper(cur.right)
        
#         def helper2(cur):
#             if not cur:
#                 return False
#             if cur.val in to_find:
#                 return True
#             ans = False
#             ans |= helper2(cur.left)
#             ans |= helper2(cur.right)
#             return ans
#         helper(root)
#         if len(to_find) < 2:
#             return False
#         return helper2(root)
        

# This solution works !!! made a set to check if we saw k-elem 
# if k-yourself = yourself then return False 
# For this approach, we assume that there is no dublicate in BST  



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        to_find = set([])
        def helper(cur):
            if not cur:
                return
            to_find.add(k-cur.val)
            helper(cur.left)
            helper(cur.right)
        
        def helper2(cur):
            if not cur:
                return False
            if cur.val in to_find and k-cur.val != cur.val:
                return True
            ans = False
            ans |= helper2(cur.left)
            ans |= helper2(cur.right)
            return ans
        helper(root)
        if len(to_find) < 2:
            return False
        return helper2(root)
        
        
        
# Another solution:

def findTarget(self, root, k):
        if not root: return False
        bfs, s = [root], set()
        for i in bfs:
            if k - i.val in s: return True
            s.add(i.val)
            if i.left: bfs.append(i.left)
            if i.right: bfs.append(i.right)
        return False