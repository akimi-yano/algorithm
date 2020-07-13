# 100. Same Tree

# Given two binary trees, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

# Example 1:

# Input:     1         1
#           / \       / \
#          2   3     2   3

#         [1,2,3],   [1,2,3]

# Output: true
# Example 2:

# Input:     1         1
#           /           \
#          2             2

#         [1,2],     [1,null,2]

# Output: false
# Example 3:

# Input:     1         1
#           / \       / \
#          2   1     1   2

#         [1,2,1],   [1,1,2]

# Output: false


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Yay this works !
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def helper(pcur,qcur):

            if pcur is None and qcur is not None:
                return False
            if pcur is not None and qcur is None:
                return False
            if pcur is None and qcur is None:
                return True
            if pcur.val != qcur.val:
                return False
            res_left = helper(pcur.left,qcur.left)
            res_right = helper(pcur.right,qcur.right)
            return res_left == res_right == True

        return helper(p,q)
        
        
# other ways ----
# p is q - It is just to return True if p==None and q==None else False.

# The "proper" way:

def isSameTree(self, p, q):
    if p and q:
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    return p is q

# The "tupleify" way:

def isSameTree(self, p, q):
    def t(n):
        return n and (n.val, t(n.left), t(n.right))
    return t(p) == t(q)

# The first way as one-liner:

def isSameTree(self, p, q):
    return p and q and p.val == q.val and all(map(self.isSameTree, (p.left, p.right), (q.left, q.right))) or p is q


# simple recursion

def isSameTree1(self, p, q):
    if p and q:
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    else:
        # if "p and q" is not satisfied, then at least one of them is None. 
        # So we need to check if they are both None.
        return p == q
    

# DFS with stack - iterative 
def isSameTree2(self, p, q):
    stack = [(p, q)]
    while stack:
        node1, node2 = stack.pop()
        if not node1 and not node2:
            continue
        elif None in [node1, node2]:
            return False
        else:
            if node1.val != node2.val:
                return False
            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))
    return True
 
# BFS with queue - iterative  
def isSameTree3(self, p, q):
    queue = [(p, q)]
    while queue:
        node1, node2 = queue.pop(0)
        if not node1 and not node2:
            continue
        elif None in [node1, node2]:
            return False
        else:
            if node1.val != node2.val:
                return False
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))
    return True