# 1339. Maximum Product of Splitted Binary Tree
# Medium

# 854

# 49

# Add to List

# Share
# Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

# Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

# Note that you need to maximize the answer before taking the mod and not after taking it.

 

# Example 1:


# Input: root = [1,2,3,4,5,6]
# Output: 110
# Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
# Example 2:


# Input: root = [1,null,2,3,4,null,null,5,6]
# Output: 90
# Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
# Example 3:

# Input: root = [2,3,9,10,7,8,6,5,4,11,1]
# Output: 1025
# Example 4:

# Input: root = [1,1]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [2, 5 * 104].
# 1 <= Node.val <= 104

# This solution works:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    MOD =  10 ** 9 + 7
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        @lru_cache(None)
        def get_total_from_cur(cur):
            if not cur:
                return 0
            return cur.val + get_total_from_cur(cur.left) + get_total_from_cur(cur.right)
        
        def get_best_prod(cur):
            nonlocal total, best
            if not cur:
                return
            if cur.left:
                left = get_total_from_cur(cur.left) 
                right = total-left
                best = max(best,left * right)
                get_best_prod(cur.left)
            if cur.right:
                right = get_total_from_cur(cur.right)
                left = total-right 
                best = max(best,left * right)
                get_best_prod(cur.right)
        
        total = get_total_from_cur(root)
        best = 0
        get_best_prod(root)
        return best % Solution.MOD