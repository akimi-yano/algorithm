# 236. Lowest Common Ancestor of a Binary Tree

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]


 

# Example 1:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# Example 2:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
 

# Note:

# All of the nodes' values will be unique.
# p and q are different and both values will exist in the binary tree.





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.p = None
        self.q = None
        self.p_ancestors = []
        self.q_ancestors = []

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q
        self.find_p_or_q(root, [])

        height = min(len(self.p_ancestors), len(self.q_ancestors)) - 1
        while height >= 0:
            if self.p_ancestors[height].val == self.q_ancestors[height].val:
                return self.p_ancestors[height]
            height -= 1
        return None
    
    def find_p_or_q(self, cur, ancestors):
        if cur is None:
            return
        ancestors.append(cur)
        if cur.val == self.p.val:
            self.p_ancestors = list(ancestors)
        elif cur.val == self.q.val:
            self.q_ancestors = list(ancestors)
        self.find_p_or_q(cur.left, ancestors)
        self.find_p_or_q(cur.right, ancestors)
        ancestors.pop()
