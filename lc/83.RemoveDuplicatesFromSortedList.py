'''
83. Remove Duplicates from Sorted List
Easy
8K
271
Companies
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
'''

# Solution with 2 variables:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
      cur = head
      prev = None
      while cur:
        if prev and cur.val == prev.val:
          prev.next = cur.next
          cur = cur.next
        else:
          prev = cur
          cur = cur.next
      return head
    
# Solution with 1 variable:
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
      '''
      1 1 2
          c n
      '''
    
      cur = head
      while cur:
        if cur.next and cur.next.val == cur.val:
          cur.next = cur.next.next
        else:
          cur = cur.next
      return head