# 116. Populating Next Right Pointers in Each Node
# Medium

# 2627

# 149

# Add to List

# Share
# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

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



# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
 

# Constraints:

# The number of nodes in the given tree is less than 4096.
# -1000 <= node.val <= 1000


# This solution works !

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
        if not root:
            return root
            
        queue = deque([root])
        
        while queue:
            new_queue = deque([])
            cur = None
            while queue:
                node = queue.popleft()
                if cur:
                    cur.next = node
                    cur = cur.next
                else:
                    cur = node
                
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
                
            queue = new_queue
        
        return root
        

# This solution works !

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
        
        parent, child = root, root.left
        while child:
            next_parent = child
            
            while parent:
                child.next = parent.right
                child = child.next
                parent = parent.next
                if parent:
                    child.next = parent.left
                child = child.next
            
            parent, child = next_parent,  next_parent.left
        return root