# 117. Populating Next Right Pointers in Each Node II
# Medium

# 2073

# 193

# Add to List

# Share
# Given a binary tree

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

 

# Follow up:

# You may only use constant extra space.
# Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
 

# Example 1:



# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
 

# Constraints:

# The number of nodes in the given tree is less than 6000.
# -100 <= node.val <= 100


# This approach works :

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        queue = deque([root])
        while queue:
            new_queue = deque([])
            while queue:
                node  = queue.popleft()
                if not queue:
                    node.next = None
                else:
                    node.next = queue[0]
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue
        return root
            

# this solution works - constant space solution

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        
        parent = root

        while True:
            start_child, parent = self.next_child(parent, None)
            if start_child is None:
                break
            cur_child = start_child
            while cur_child is not None:
                nxt, parent = self.next_child(parent, cur_child)
                cur_child.next = nxt
                cur_child = nxt
            parent = start_child
        return root
    
    def next_child(self, parent, prev_child):
        while parent is not None:
            if parent.left is not None and prev_child != parent.left:
                return parent.left, parent
            elif parent.right is not None and prev_child != parent.right:
                return parent.right, parent.next
            else:
                parent = parent.next
        return None, None