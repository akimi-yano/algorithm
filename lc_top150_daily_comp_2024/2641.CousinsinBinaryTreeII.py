'''
2641. Cousins in Binary Tree II
Solved
Medium
Topics
Companies
Hint
Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Return the root of the modified tree.

Note that the depth of a node is the number of edges in the path from the root node to it.

 

Example 1:


Input: root = [5,4,9,1,10,null,7]
Output: [0,0,0,7,7,null,11]
Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
- Node with value 5 does not have any cousins so its sum is 0.
- Node with value 4 does not have any cousins so its sum is 0.
- Node with value 9 does not have any cousins so its sum is 0.
- Node with value 1 has a cousin with value 7 so its sum is 7.
- Node with value 10 has a cousin with value 7 so its sum is 7.
- Node with value 7 has cousins with values 1 and 10 so its sum is 11.
Example 2:


Input: root = [3,1,2]
Output: [0,0,0]
Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
- Node with value 3 does not have any cousins so its sum is 0.
- Node with value 1 does not have any cousins so its sum is 0.
- Node with value 2 does not have any cousins so its sum is 0.
 

Constraints:

The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 104
'''

# BFS Approach:

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS traversal to get next level sum, get the sum of each level
        # During traversal, find the nodes with 2 kids and update the value of each kid 
        # to the sum of the 2kids
        # for each node use level sum to minus its updated value to get final value.

        # calculate the node's value
        queue = deque([(root)])
        cur_level_sum = root.val

        while queue:
            next_queue = deque([])
            next_level_sum = 0
            while queue:
                node = queue.popleft()
                node.val = cur_level_sum - node.val

                if node.left:
                    next_queue.append(node.left)
                    next_level_sum += node.left.val
                if node.right:
                    next_queue.append(node.right)
                    next_level_sum += node.right.val
                
                if node.left and node.right:
                    siblings_sum = node.left.val + node.right.val
                    node.left.val = node.right.val = siblings_sum
            
            queue = next_queue
            cur_level_sum = next_level_sum
        
        return root

# DFS Approach:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 1 DFS to get the sum of each level
        # 2 DFS to locate the nodes with 2 kids and update the val of each kid to the 
        # sum of the 2 kids and for each node, use level sum to minus its updated val to get final val

        def dfs_for_sum(node, level):
            if level == len(level_sum):
                level_sum.append(0)
            level_sum[level] += node.val
            if node.left:
                dfs_for_sum(node.left, level+1)
            if node.right:
                dfs_for_sum(node.right, level+1)

        def dfs_for_update(node, level):
            node.val = level_sum[level] - node.val
            if node.left and node.right:
                siblings_sum = node.left.val + node.right.val
                node.left.val = node.right.val = siblings_sum
            if node.left:
                dfs_for_update(node.left, level+1)
            if node.right:
                dfs_for_update(node.right, level+1)

        level_sum = []
        dfs_for_sum(root, 0)
        dfs_for_update(root, 0)
        return root