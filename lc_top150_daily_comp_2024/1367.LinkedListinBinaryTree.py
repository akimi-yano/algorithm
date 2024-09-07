'''
1367. Linked List in Binary Tree
Solved
Medium
Topics
Companies
Hint
Given a binary tree root and a linked list with head as the first node. 

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.

 

Example 1:



Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Explanation: Nodes in blue form a subpath in the binary Tree.  
Example 2:



Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Example 3:

Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: false
Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.
 

Constraints:

The number of nodes in the tree will be in the range [1, 2500].
The number of nodes in the list will be in the range [1, 100].
1 <= Node.val <= 100 for each node in the linked list and binary tree.
'''

# This solution works:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        @cache
        def helper(tree_cur, linked_list_cur):
            if not linked_list_cur:
                return True
            if not tree_cur:
                return False

            ans = False
            # use it if the val matches
            if tree_cur.val == linked_list_cur.val:
                ans |= helper(tree_cur.left, linked_list_cur.next)
                ans |= helper(tree_cur.right, linked_list_cur.next)
            # not use it if the val does not watch or match (cuz it could fail at the end or middle)
            # so always have this option to start from head again
            ans |= helper(tree_cur.left, head)
            ans |= helper(tree_cur.right, head)
           
            return ans
        return helper(root, head)

# Time: O(L*T)
# Space: O(L*T)