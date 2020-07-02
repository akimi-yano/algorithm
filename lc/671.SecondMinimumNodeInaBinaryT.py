# 671. Second Minimum Node In a Binary Tree

# Given a non-empty special binary tree consisting of nodes with the non-negative value, 
# where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, 
# then this node's value is the smaller value among its two sub-nodes. More formally, 
# the property root.val = min(root.left.val, root.right.val) always holds.

# Given such a binary tree, you need to output the second minimum value in the set made of all 
# the nodes' value in the whole tree.

# If no such second minimum value exists, output -1 instead.

# Example 1:

# Input: 
#     2
#    / \
#   2   5
#      / \
#     5   7

# Output: 5
# Explanation: The smallest value is 2, the second smallest value is 5.
 

# Example 2:

# Input: 
#     2
#    / \
#   2   2

# Output: -1
# Explanation: The smallest value is 2, but there isn't any second smallest value.
    
    
    
    
# another example to keep in mind:
# Input:
# [1,1,3,1,1,3,4,3,1,1,1,3,8,4,8,3,3,1,6,2,1]
# Output: 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:

# this works but slow - DFS and keep track of min that is larger than root.val 
# (return if its larger than root.val)
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1
        
        def helper(current,val):
            if current is None:
                return float('inf')
            if current.val > val:
                return current.val
            min_score = float('inf')
            left = helper(current.left,val)
            right = helper(current.right,val)
            min_score = min(min_score,left,right)
            # print(max_score,val)
            return min_score
        ans = helper(root,root.val)
        return -1 if ans == float('inf') else ans
    
    
    
    
    # this is a BFS approach and it did not work due to the 3rd example test case
    # you might find smaller value at a deeper level of a tree so you need to check everything
    
    # def findSecondMinimumValue(self, root: TreeNode) -> int:
        # queue = deque([root])
        # target = root.val
        # seen = set([root])
        # while queue:
        #     # print(queue)
        #     cur = queue.pop()
        #     if cur.val > target:
        #         return cur.val
        #     if cur.left:
        #         if cur.left not in seen:
        #             queue.append(cur.left)
        #             seen.add(cur.left)
        #         if cur.right not in seen:
        #             queue.append(cur.right)
        #             seen.add(cur.right)
        # return -1
            
            
            
            
# Based on the special property of the tree, we can guarantee that the root node is 
# the smallest node in the tree. We just have to recursively traverse the tree and 
# find a node that is bigger than the root node but smaller than any existing node we have come across.

# same approach but faster 
class Solution(object):
    def findSecondMinimumValue(self, root):
        res = [float('inf')]
        def traverse(node):
            if not node:
                return
            if root.val < node.val < res[0]:
                res[0] = node.val
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return -1 if res[0] == float('inf') else res[0]
            


# cleaned up my original code by having a global variable and update it instead of returning 

    def findSecondMinimumValue(self, root: TreeNode) -> int:

        self.min = float('inf')
        def helper(current,val):
            if current is None:
                return 
            if self.min > current.val > val:
                self.min = current.val
            helper(current.left,val)
            helper(current.right,val)
            
        helper(root,root.val)
        
        return -1 if self.min == float('inf') else self.min
            


# optimization -  we only need to do dfs when root.val == node.val
# also set the root_val as a global variable

def findSecondMinimumValue(self, root: TreeNode) -> int:
def findSecondMinimumValue(self, root: TreeNode) -> int:
    self.root_val = root.val
    self.second = float(inf)

    def dfs(node):
        if node:
            if self.root_val < node.val < self.second:
                self.second = node.val
            if self.root_val == node.val:
                dfs(node.left)
                dfs(node.right)
    dfs(root)
    return self.second if self.second!=float('inf') else -1