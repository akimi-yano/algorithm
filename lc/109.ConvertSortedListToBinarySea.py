# 109. Convert Sorted List to Binary Search Tree
# Medium

# 3108

# 98

# Add to List

# Share
# Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

 

# Example 1:


# Input: head = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
# Example 2:

# Input: head = []
# Output: []
# Example 3:

# Input: head = [0]
# Output: [0]
# Example 4:

# Input: head = [1,3]
# Output: [3,1]
 

# Constraints:

# The number of nodes in head is in the range [0, 2 * 104].
# -10^5 <= Node.val <= 10^5


# this approach does not work:

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def sortedListToBST(self, head: ListNode) -> TreeNode:
#         def helper(cur):
#             if not cur:
#                 return 0
#             left = helper(cur.left)
#             right = helper(cur.right)
#             diff = (left-right)
#             if diff  > 1:
#                 return float('-inf')
#             else:
#                 return 1 + left + right
               
#         newhead = TreeNode(None)
#         cur = head
#         while cur:
#             val = helper(head)
#             if val == float('inf'):
#                 nextnode = newhead.right
#                 newhead.right = cur
#                 cur.right = nextnode               
#             elif val == float('-inf'):
#                 nextnode = newhead.left
#                 newhead.left = cur
#                 cur.left = nextnode
#             else:
#                 nextnode = newhead.next
#                 newhead.next = cur
#                 cur.next = nextnode
#         return newhead.next


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
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def helper(list_node, size):
            if not size:
                return None
            if size == 1:
                return TreeNode(val=list_node.val)
            
            # recursion for left side
            left_treenode = helper(list_node, size // 2)
            
            cur = list_node
            
            # make middle tree node
            for _ in range(size // 2):
                cur = cur.next
            mid_treenode = TreeNode(cur.val)
            
            # recursion for right side
            right_treenode = helper(cur.next, (size-1) // 2)
            
            # connect the left and right tree nodes to mid treenode
            mid_treenode.left = left_treenode
            mid_treenode.right = right_treenode
            
            return mid_treenode
            
            
               
        total = 0
        cur = head
        while cur:
            total += 1
            cur = cur.next
        if not total:
            return None
        return helper(head, total)
        