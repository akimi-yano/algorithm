# 21. Merge Two Sorted Lists
# Easy

# 11042

# 1012

# Add to List

# Share
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.


# This solution works:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def helper(cur1, cur2):
            if not cur1:
                return cur2
            if not cur2:
                return cur1
            if cur1.val < cur2.val:
                cur1.next = helper(cur1.next, cur2)
                return cur1
            else:
                cur2.next = helper(cur1, cur2.next)
                return cur2
        return helper(list1, list2)