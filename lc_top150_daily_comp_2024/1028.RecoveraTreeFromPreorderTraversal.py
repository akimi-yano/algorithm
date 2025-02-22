'''
1028. Recover a Tree From Preorder Traversal
Hard
Topics
Companies
Hint
We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its root.

 

Example 1:


Input: traversal = "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]
Example 2:


Input: traversal = "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]
Example 3:


Input: traversal = "1-401--349---90--88"
Output: [1,401,null,349,88,90]
 

Constraints:

The number of nodes in the original tree is in the range [1, 1000].
1 <= Node.val <= 109
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        traversal = traversal + '+'
        dummy = TreeNode(None)
        stack = [(-1, dummy)] # (depth, node)
        num = 0
        depth = 0
        is_prev_numeric = False
        for elem in traversal:
            if elem.isnumeric():
                if not is_prev_numeric:
                    num = 0
                num *= 10
                num += int(elem)          
                is_prev_numeric = True
            else:
                if is_prev_numeric:            
                    new_node = TreeNode(num)
                    while stack[-1][0] >= depth:
                        _, n = stack.pop()
                    if not stack[-1][1].left:
                        stack[-1][1].left = new_node
                    else:
                        stack[-1][1].right = new_node
                    stack.append((depth, new_node))
                    depth = 0
                depth += 1
                is_prev_numeric = False

        return dummy.left        

# Improvement:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        i = 0
        while i < len(traversal):
            depth = 0
            val = 0
            while i < len(traversal) and traversal[i] == '-':
                depth += 1
                i += 1
            while i < len(traversal) and traversal[i] != '-':
                val *= 10 
                val += int(traversal[i])
                i += 1
            while len(stack) > depth:
                stack.pop()
            new_node = TreeNode(val)
            if stack and not stack[-1].left:
                stack[-1].left = new_node  
            elif stack:
                stack[-1].right = new_node
            stack.append(new_node)
        return stack[0]

# Time: O(N)
# Space: O(N)
