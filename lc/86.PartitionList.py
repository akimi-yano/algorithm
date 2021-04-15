# 86. Partition List
# Medium

# 2146

# 393

# Add to List

# Share
# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

 

# Example 1:


# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
# Example 2:

# Input: head = [2,1], x = 2
# Output: [1,2]
 

# Constraints:

# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200

# This solution works:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        smaller_cur = smaller_head = ListNode(None)
        larger_eq_cur = larger_eq_head = ListNode(None)
        cur = head
        while cur:
            if cur.val < x:
                smaller_cur.next = cur
                cur = cur.next
                smaller_cur = smaller_cur.next
                smaller_cur.next = None
            else:
                larger_eq_cur.next = cur
                cur = cur.next
                larger_eq_cur = larger_eq_cur.next
                larger_eq_cur.next = None
        smaller_cur.next = larger_eq_head.next
        return smaller_head.next