# 61. Rotate List
# Medium

# 4352

# 1250

# Add to List

# Share
# Given the head of a linked list, rotate the list to the right by k places.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:


# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
 

# Constraints:

# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109


# This solution works:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        1 2 3 4 5
              len-k
        '''
        n = 0
        cur = head
        while cur:
            cur = cur.next
            n += 1
        if n == 0:
            return head
        k = k % n
        if k == 0:
            return head
        cur = head
        newhead, prev = None, None
        for _ in range(n-k):
            prev = cur
            cur = cur.next
        newhead = cur
        prev.next = None
        newcur = newhead
        prev = None
        while newcur:
            prev = newcur
            newcur = newcur.next
        prev.next = head
        return newhead