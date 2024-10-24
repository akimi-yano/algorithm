# 92. Reverse Linked List II
# Medium

# 4079

# 212

# Add to List

# Share
# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [5], left = 1, right = 1
# Output: [5]
 

# Constraints:

# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
 

# Follow up: Could you do it in one pass?

# This solution works:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        '''
        1 2 3 4 5
       s1 - - - e1
          cur-3
         count how many nodes I need to reverse and reverse num nodes from the cur node
        '''
        # this function reverses all the nodes from cur to the count and returns the new head
        def reverse(cur, count):
            prev = None
            temp = cur
            while count:
                nextn = cur.next
                cur.next = prev
                prev = cur
                cur = nextn
                count -= 1
            temp.next = cur
            return prev
    
        # edge case - if left and right are the same, no need to swap
        if left == right:
            return head
        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        cur = head
        idx = 1
        # find the starting node and count
        while idx < left:
            prev, cur = cur, cur.next
            idx += 1
        num = right - left + 1
        prev.next = reverse(cur, num)
        return dummy.next
            