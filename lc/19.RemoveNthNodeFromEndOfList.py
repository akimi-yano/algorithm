# 19. Remove Nth Node From End of List
# Medium

# 5202

# 302

# Add to List

# Share
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Follow up: Could you do this in one pass?

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

# This solution works:

'''
get the length and find out how many from front
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1
        num_from_front = length - n -1
        
        if num_from_front < 0:
            return head.next
        
        cur = head
        while num_from_front:
            cur = cur.next
            num_from_front -= 1
        cur.next = cur.next.next

        return head