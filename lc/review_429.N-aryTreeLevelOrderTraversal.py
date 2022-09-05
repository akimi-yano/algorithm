# 429. N-ary Tree Level Order Traversal
# Medium

# 2447

# 104

# Add to List

# Share
# Given an n-ary tree, return the level order traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

# Example 1:



# Input: root = [1,null,3,2,4,null,5,6]
# Output: [[1],[3,2,4],[5,6]]
# Example 2:



# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
 

# Constraints:

# The height of the n-ary tree is less than or equal to 1000
# The total number of nodes is between [0, 104]


# This solution works:


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        ans = []
        
        while queue:
            new_queue = deque([])
            new_row = []
            while queue:
                node = queue.popleft()
                new_row.append(node.val)
                for next_node in node.children:
                    new_queue.append(next_node)
            queue = new_queue
            ans.append(new_row)
        return ans