# 148. Sort List
# Medium

# 3381

# 149

# Add to List

# Share
# Given the head of a linked list, return the list after sorting it in ascending order.

# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

 

# Example 1:


# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# Example 2:


# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is in the range [0, 5 * 104].
# -105 <= Node.val <= 105



# This solution works !


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        self.N = 0
        cur = head
        while cur is not None:
            self.N += 1
            cur = cur.next
        size = 1
        while size < self.N:
            #1. merge
            new_head = None
            prev_last = None
            cur = head
            while cur is not None:
                first, last = self.merge(cur, size)
                if new_head is None:
                    new_head = first
                else:
                    prev_last.next = first
                prev_last = last
                cur = prev_last.next
            #2. double the size
            # same as multiplying by 2 (size *= 2)
            size <<= 1
            head = new_head
        return head
    
    def merge(self, cur, size):
        # print('before merge with size {}:\nhead {}\n'.format(size, cur))
        i = 0
        first = second = cur
        while i < size and second.next is not None:
            second = second.next
            i += 1
        # if we didn't reach the second list, return as-is.
        if i < size:
            return first, second
        
        first_count = 0
        second_count = 0
        head = cur = None
        while first_count < size and second_count < size and second is not None:
            if first.val < second.val:
                if head is None:
                    head = first
                else:
                    cur.next = first
                cur = first
                first = first.next
                first_count += 1
            else:
                if head is None:
                    head = second
                else:
                    cur.next = second
                cur = second
                second = second.next
                second_count += 1
        while first_count < size:
            cur.next = first
            cur = first
            first = first.next
            first_count += 1
        while second_count < size and second is not None:
            cur.next = second
            cur = second
            second = second.next
            second_count += 1
    
        cur.next = second
        
        # print('after merge\nhead {}\ntail {}\n'.format(head, cur))
        return head, cur