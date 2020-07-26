# 1530. Number of Good Leaf Nodes Pairs

# Given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.

# Return the number of good leaf node pairs in the tree.

 

# Example 1:


# Input: root = [1,2,3,null,4], distance = 3
# Output: 1
# Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.
# Example 2:


# Input: root = [1,2,3,4,5,6,7], distance = 3
# Output: 2
# Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of ther shortest path between them is 4.
# Example 3:

# Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
# Output: 1
# Explanation: The only good pair is [2,5].
# Example 4:

# Input: root = [100], distance = 1
# Output: 0
# Example 5:

# Input: root = [1,1,1], distance = 2
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [1, 2^10].
# Each node's value is between [1, 100].
# 1 <= distance <= 10





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# this solution does not work

# class Solution:
#     def countPairs(self, root: TreeNode, distance: int) -> int:
#         self.dist= distance
#         self.pairs = 0
#         def helper(cur):
#             # print(cur)
#             if not cur.left and not cur.right:
#                 return 1
#             left = 0
#             right = 0
#             if cur.left:
#                 left = helper(cur.left)
#             if cur.right:
#                 right = helper(cur.right)
#             total = left+right +1
#             if total<=self.dist :
#                 self.pairs+=1
#             return total
#         helper(root)
#         return self.pairs



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# this works !!!!! - return arr to keep track of multiple leaf nodes
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.dist= distance
        self.pairs = 0
        def helper(cur):
            # print(cur)
            if not cur.left and not cur.right:
                return [1]
            left = []
            right = []
            if cur.left:
                left = helper(cur.left)
            if cur.right:
                right = helper(cur.right)
            for l in left:
                for r in right:
                    if l + r <= self.dist:
                        self.pairs += 1
            return [1+l for l in left] + [1+r for r in right]
        helper(root)
        return self.pairs








            