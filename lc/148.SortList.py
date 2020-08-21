# 148. Sort List

# Sort a linked list in O(n log n) time using constant space complexity.

# Example 1:

# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:

# Input: -1->5->3->4->0
# Output: -1->0->3->4->5


# This solution works but it is not constant space - but I like it - using merge sort 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
4->2->1->3
  4, 2 => 2->4
  1, 3 => 1->3
 2->4->1->3
  2->4, 1->3 => 1->2->3->4
'''
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        size = 0
        cur = head
        while cur is not None:
            size, cur = size + 1, cur.next
        
        return self.merge(head, size)
    
    def merge(self, cur, size):
        if size < 2:
            return cur

        left_unsorted = right_unsorted = cur
        # move right_unsorted to one before the beginning of the second half
        for i in range((size - 1) // 2):
            right_unsorted = right_unsorted.next
        right_unsorted.next, right_unsorted = None, right_unsorted.next
    
        left_size = (size + 1) // 2
        right_size = size - left_size

        left_sorted = self.merge(left_unsorted, left_size)
        right_sorted = self.merge(right_unsorted, right_size)
        
        head = cur = None
        while left_sorted is not None and right_sorted is not None:
            if left_sorted.val <= right_sorted.val:
                if head is None:
                    head = cur = left_sorted
                else:
                    cur.next = left_sorted
                    cur = cur.next
                left_sorted = left_sorted.next
            else:
                if head is None:
                    head = cur = right_sorted
                else:
                    cur.next = right_sorted
                    cur = cur.next
                right_sorted = right_sorted.next
        if left_sorted is not None:
            cur.next = left_sorted
        else:
            cur.next = right_sorted
        return head