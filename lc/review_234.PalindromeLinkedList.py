# 234. Palindrome Linked List
# Easy

# 4992

# 432

# Add to List

# Share
# Given the head of a singly linked list, return true if it is a palindrome.

 

# Example 1:


# Input: head = [1,2,2,1]
# Output: true
# Example 2:


# Input: head = [1,2]
# Output: false
 

# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9
 

# Follow up: Could you do it in O(n) time and O(1) space?

# This solution works:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow
        
        prev = None
        cur = mid
        while cur:
            nextnode = cur.next
            cur.next = prev
            prev = cur
            cur = nextnode
        start2 = prev
        start1 = head

        while start1 and start2:
            if start1.val != start2.val:
                return False
            start1 = start1.next
            start2 = start2.next
        return True
    