# 148. Sort List
# Medium

# 6025

# 204

# Add to List

# Share
# Given the head of a linked list, return the list after sorting it in ascending order.

 

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
 

# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?


# This solution works:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next
            
        arr.sort(key=lambda x: x.val)
        for elem in arr:
            elem.next = None
            
        for i in range(min(1, len(arr)), len(arr)):
            arr[i-1].next = arr[i]
        
        return arr[0] if arr else None