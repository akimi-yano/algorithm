# 61. Rotate List
# Medium

# 1628

# 1063

# Add to List

# Share
# Given a linked list, rotate the list to the right by k places, where k is non-negative.

# Example 1:

# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
# Example 2:

# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL


# This approach does not work : 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def rotateRight(self, head: ListNode, k: int) -> ListNode:
#         if not head:
#             return None
#         if k == 0:
#             return head
        
#         length = 0
#         cur = head
#         while cur:
#             length += 1
#             cur = cur.next
        
#         if length <2:
#             return head
            
#         kth = k % length
#         before_kth = length - kth
        
#         if kth <1:
#             return head

#         '''
#         before: before_kth -> kth -> None
#         after: kth -> before_kth -> None
#         '''
#         cur = head
#         if length % 2 == 0:
#             even = 1
#         else:
#             even = 0
#         while kth - even:
#             kth -= 1
#             cur = cur.next 
#         print(cur.val)
#         kthhead = cur.next 
#         cur.next = None
        
        
#         cur= kthhead
#         while cur and cur.next:
#             cur = cur.next
#         lastnode = cur
        
#         lastnode.next = head
#         head = kthhead
        
#         return head
    
    
    
# This solution works:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # edge case
        if not head or not k:
            return head
        
        # find out the length
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        # if the length is 1, no rotation, return head
        if length <2:
            return head
            
        rotateTimes = k % length
        
        # if the totation times is 0 return head 
        if rotateTimes <1:
            return head
        
        # start both pointers from head
        fastPointer = head
        slowPointer = head
        
        # only move the fast pointer by the time of rotate times
        for _ in range(rotateTimes):
            fastPointer = fastPointer.next
        '''
        1->2->3->4->5->NULL, k = 2
             (f) <- moved 2 times
        (s)
        
                   (f)
              (s)temp
        1->2->3->None
        4->5->(head)1->2->3->None
        (head)4->5->1->2->3->None
        '''
        while fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next

        temp = slowPointer.next

        slowPointer.next = None
        fastPointer.next = head
        head = temp
       
        return head
        
        
# This solution works !

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if k == 0:
            return head
        
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        if length <2:
            return head
            
        kth = k % length
        before_kth = length - kth - 1
        
        if kth <1:
            return head
        '''
        before: before_kth -> kth -> None
        after: kth -> before_kth -> None
        '''
        cur = head

        while before_kth:
            before_kth -= 1
            cur = cur.next 
        
        kthhead = cur.next 
        cur.next = None
        
        cur= kthhead
        while cur and cur.next:
            cur = cur.next
        lastnode = cur
        
        lastnode.next = head
        head = kthhead
        
        return head
        