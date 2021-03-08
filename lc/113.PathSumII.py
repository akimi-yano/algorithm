# 113. Path Sum II
# Medium

# 2575

# 85

# Add to List

# Share
# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.

# A leaf is a node with no children.



# Example 1:


# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# Example 2:


# Input: root = [1,2,3], targetSum = 5
# Output: []
# Example 3:

# Input: root = [1,2], targetSum = 0
# Output: []


# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000



# This solution works:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def helper(cur, total):
            nonlocal targetSum
            if not cur:
                return []
            if not cur.left and not cur.right and total+cur.val == targetSum:
                return [[cur.val]]
            arr =[]
            arr.extend([cur.val] + temp for temp in helper(cur.left, total+cur.val))
            arr.extend([cur.val] + temp for temp in helper(cur.right, total+cur.val))
            return arr
        return helper(root, 0)
                
                
                
# This solution works - optimization:


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = {}
        for c in s1:
            if c not in counter:
                counter[c] = 0
            counter[c] += 1
        for c in s2[:len(s1)]:
            if c not in counter:
                counter[c] = 0
            counter[c] -= 1
            if not counter[c]:
                del counter[c]
        if not counter:
            return True

        for nxt in range(len(s1), len(s2)):
            add_c = s2[nxt]
            del_c = s2[nxt-len(s1)]
            if add_c not in counter:
                counter[add_c] = 0
            if del_c not in counter:
                counter[del_c] = 0
            counter[add_c] -= 1
            counter[del_c] += 1
            if not counter[add_c]:
                del counter[add_c]
            if del_c in counter and not counter[del_c]:
                del counter[del_c]
            if not counter:
                return True
        return False
        