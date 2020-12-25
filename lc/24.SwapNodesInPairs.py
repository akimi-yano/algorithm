# 24. Swap Nodes in Pairs
# Medium

# 3061

# 197

# Add to List

# Share
# Given a linked list, swap every two adjacent nodes and return its head.

# You may not modify the values in the list's nodes. Only nodes itself may be changed.

 

# Example 1:


# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# Example 2:

# Input: head = []
# Output: []
# Example 3:

# Input: head = [1]
# Output: [1]
 

# Constraints:

# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100

# This solution works

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        cur = head
        arr = []
        while cur:
            arr.append(cur)
            cur = cur.next
            
        for node in arr:
            node.next = None
        
        for i in range(0, len(arr)-1, 2):
            arr[i], arr[i+1] =  arr[i+1], arr[i]
            
        
        for i in range(len(arr)-1):
            arr[i].next = arr[i+1]
        
        head = arr[0]
        return head


# This solution works - optimization

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        if not head.next:
            return head
        first = head.next
        second = head
        first.next, second.next = second, first.next
        head = first
        prev = second
        cur = second.next
        while cur and cur.next:
            first = cur.next
            second = cur
            prev.next = first
            first.next, second.next = second, first.next
            prev = second
            cur = second.next
        
        return head