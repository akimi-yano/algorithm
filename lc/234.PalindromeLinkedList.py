# 234. Palindrome Linked List
# Easy

# 10784

# 627

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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        cur = head
        length = 0
        while cur:
            cur = cur.next
            length += 1
        half = length // 2
        cur = head
        while cur and half:
            stack.append(cur.val)
            cur = cur.next
            half -= 1
        if cur and length % 2:
            cur = cur.next
        while cur and stack:
            val = stack.pop()
            if cur.val != val:
                return False
            cur = cur.next
        return True