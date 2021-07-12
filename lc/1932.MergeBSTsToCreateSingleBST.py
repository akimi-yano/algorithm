# 1932. Merge BSTs to Create Single BST
# Hard

# 51

# 2

# Add to List

# Share
# You are given n BST (binary search tree) root nodes for n separate BSTs stored in an array trees (0-indexed). Each BST in trees has at most 3 nodes, and no two roots have the same value. In one operation, you can:

# Select two distinct indices i and j such that the value stored at one of the leaves of trees[i] is equal to the root value of trees[j].
# Replace the leaf node in trees[i] with trees[j].
# Remove trees[j] from trees.
# Return the root of the resulting BST if it is possible to form a valid BST after performing n - 1 operations, or null if it is impossible to create a valid BST.

# A BST (binary search tree) is a binary tree where each node satisfies the following property:

# Every node in the node's left subtree has a value strictly less than the node's value.
# Every node in the node's right subtree has a value strictly greater than the node's value.
# A leaf is a node that has no children.

 

# Example 1:


# Input: trees = [[2,1],[3,2,5],[5,4]]
# Output: [3,2,5,1,null,4]
# Explanation:
# In the first operation, pick i=1 and j=0, and merge trees[0] into trees[1].
# Delete trees[0], so trees = [[3,2,5,1],[5,4]].

# In the second operation, pick i=0 and j=1, and merge trees[1] into trees[0].
# Delete trees[1], so trees = [[3,2,5,1,null,4]].

# The resulting tree, shown above, is a valid BST, so return its root.
# Example 2:


# Input: trees = [[5,3,8],[3,2,6]]
# Output: []
# Explanation:
# Pick i=0 and j=1 and merge trees[1] into trees[0].
# Delete trees[1], so trees = [[5,3,8,2,6]].

# The resulting tree is shown above. This is the only valid operation that can be performed, but the resulting tree is not a valid BST, so return null.
# Example 3:


# Input: trees = [[5,4],[3]]
# Output: []
# Explanation: It is impossible to perform any operations.
# Example 4:


# Input: trees = [[2,1,3]]
# Output: [2,1,3]
# Explanation: There is only one tree, and it is already a valid BST, so return its root.
 

# Constraints:

# n == trees.length
# 1 <= n <= 5 * 104
# The number of nodes in each tree is in the range [1, 3].
# No two roots of trees have the same value.
# All the trees in the input are valid BSTs.
# 1 <= TreeNode.val <= 5 * 104.

# This solution works:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def canMerge(self, trees: List[TreeNode]) -> TreeNode:
        roots = {}
        for root in trees:
            if root.val in roots:
                return None
            roots[root.val] = root
        
        def helper(cur):
            nonlocal old_count
            if not cur:
                return
            old_count += 1
            if (not cur.left) and (not cur.right) and cur.val in roots and cur is not roots[cur.val]:
                to_return = roots[cur.val]
                old_count -= 1
                del roots[cur.val]
                return to_return
            cur.left = helper(cur.left)
            cur.right = helper(cur.right)
            return cur
        
        old_count = 0
        for root in trees:
            helper(root)
  
        def validate(cur, upper, lower):
            nonlocal new_count
            if not cur:
                return True
            new_count += 1
            return lower < cur.val < upper and validate(cur.left, cur.val, lower) and validate(cur.right, upper, cur.val)
        
        if len(roots) > 1:
            return None
        new_count = 0
        for root in trees:
            if root.val in roots and validate(root, float('inf'), float('-inf')) and new_count == old_count:
                return root
        return None
