# 968. Binary Tree Cameras
# Hard

# 1561

# 22

# Add to List

# Share
# Given a binary tree, we install cameras on the nodes of the tree. 

# Each camera at a node can monitor its parent, itself, and its immediate children.

# Calculate the minimum number of cameras needed to monitor all nodes of the tree.

 

# Example 1:


# Input: [0,0,null,0,0]
# Output: 1
# Explanation: One camera is enough to monitor all nodes if placed as shown.
# Example 2:


# Input: [0,0,null,0,null,0,null,null,0]
# Output: 2
# Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.

# Note:

# The number of nodes in the given tree will be in the range [1, 1000].
# Every node has value 0.


# This solution works:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        
        # state is one of:
        # 0 - cur is already monitored
        # 1 - cur is not monitored, but can ask child to put a camera
        # 2 - cur's parent is not monitored, and has to put a camera
        @lru_cache(None)
        def helper(cur, state):
            # you always have the option to put a new camera
            best = 1
            if cur.left:
                best += helper(cur.left, 0)
            if cur.right:
                best += helper(cur.right, 0)
            
            # cur is already monitored
            if state == 0:
                maybe = 0
                if cur.left:
                    maybe += helper(cur.left, 1)
                if cur.right:
                    maybe += helper(cur.right, 1)
                best = min(best, maybe)
            elif state == 1:
                if cur.left or cur.right:
                    if cur.left:
                        maybe = helper(cur.left, 2)
                        if cur.right:
                            maybe += helper(cur.right, 1)
                        best = min(best, maybe)
                    if cur.right:
                        maybe = helper(cur.right, 2)
                        if cur.left:
                            maybe += helper(cur.left, 1)
                        best = min(best, maybe)
            elif state == 2:
                pass
            
            return best
        
        return helper(root, 1)