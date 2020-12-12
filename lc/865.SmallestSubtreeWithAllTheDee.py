# 865. Smallest Subtree with all the Deepest Nodes
# Medium

# 1015

# 272

# Add to List

# Share
# Given the root of a binary tree, the depth of each node is the shortest distance to the root.

# Return the smallest subtree such that it contains all the deepest nodes in the original tree.

# A node is called the deepest if it has the largest depth possible among any node in the entire tree.

# The subtree of a node is tree consisting of that node, plus the set of all descendants of that node.

# Note: This question is the same as 1123: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/



# Example 1:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4]
# Output: [2,7,4]
# Explanation: We return the node with value 2, colored in yellow in the diagram.
# The nodes coloured in blue are the deepest nodes of the tree.
# Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.
# Example 2:

# Input: root = [1]
# Output: [1]
# Explanation: The root is the deepest node in the tree.
# Example 3:

# Input: root = [0,1,3,null,2]
# Output: [2]
# Explanation: The deepest node in the tree is 2, the valid subtrees are the subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.


# Constraints:

# The number of nodes in the tree will be in the range [1, 500].
# 0 <= Node.val <= 500
# The values of the nodes in the tree are unique.



# This approach does not work :

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
#         return self.helper(root)[1]
    
#     def helper(self, node):
#         if node is None:
#             return 0, node
#         ldepth = self.helper(node.left)
#         rdepth = self.helper(node.right)

#         if ldepth < rdepth:
#             return rdepth + 1
#         elif ldepth > rdepth:
#             return ldepth + 1
#         else:
#             return ldepth + 1, node



# This approach does not work :

        # def helper(cur, arr):
        #     if not cur.left and not cur.right:
        #         return (1, arr + [cur]) 
        #     if not cur.left:
        #         right = helper(cur.right, arr)
        #         return (1 + right[0],  arr+ [cur])
        #     if not cur.right:
        #         left = helper(cur.left, arr)
        #         return (1 + left[0],  arr+ [cur])
        #     left = helper(cur.left, arr)
        #     right = helper(cur.right, arr)
        #     if left[0] > right[0]:
        #         return (1 + left[0], arr + [cur] + [left[1]])
        #     else:
        #         return (1 + right[0], arr + [cur] + [right[1]])
        
        # print(helper(root, []))



# This solution works :    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def helper(cur):
            if not cur:
                return (0, cur)
            left = helper(cur.left)
            right = helper(cur.right)
            
            if left[0] == right[0]:
                return (left[0] +  1, cur)
            elif left[0] > right[0]:
                return (left[0] + 1, left[1])
            else:
                return (right[0] + 1, right[1])
        
        return helper(root)[1]