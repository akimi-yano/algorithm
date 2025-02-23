'''
889. Construct Binary Tree from Preorder and Postorder Traversal
Medium
Topics
Companies
Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.

 

Example 1:


Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
Example 2:

Input: preorder = [1], postorder = [1]
Output: [1]
 

Constraints:

1 <= preorder.length <= 30
1 <= preorder[i] <= preorder.length
All the values of preorder are unique.
postorder.length == preorder.length
1 <= postorder[i] <= postorder.length
All the values of postorder are unique.
It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        '''
        preorder = [1,2,4,5,3,6,7]
                        -
        postorder = [4,5,2,6,7,3,1]
                     -
        stack: [1, 2]
        '''
        post_i = 0
        dummy = TreeNode(float('inf'))
        stack = [dummy]
        for pre_i in range(len(preorder)):
            new_node = TreeNode(preorder[pre_i])

            if preorder[pre_i] == postorder[post_i]:
                if not stack[-1].left:
                    stack[-1].left = new_node
                elif not stack[-1].right:
                    stack[-1].right = new_node
                post_i += 1
            elif preorder[pre_i] != postorder[post_i]:
                if not stack[-1].left:
                    stack[-1].left = new_node
                elif not stack[-1].right:
                    stack[-1].right = new_node
                stack.append(new_node)
            
            # Make sure to use while loop as there might be just left left left left ...
            while post_i < len(postorder) and postorder[post_i] == stack[-1].val:
                stack.pop()
                post_i += 1
        
        return dummy.left
