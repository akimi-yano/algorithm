# 25. Reverse Nodes in k-Group
# Hard

# 4406

# 427

# Add to List

# Share
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Example 2:


# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
# Example 3:

# Input: head = [1,2,3,4,5], k = 1
# Output: [1,2,3,4,5]
# Example 4:

# Input: head = [1], k = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is in the range sz.
# 1 <= sz <= 5000
# 0 <= Node.val <= 1000
# 1 <= k <= sz
 

# Follow-up: Can you solve the problem in O(1) extra memory space?

# This solution works:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cur = head
        ans = []
        count = 0
        while cur:
            temp = []
            while count < k and cur:
                temp.append(cur)
                cur = cur.next
                count += 1
            if len(temp) >= k:
                ans.extend(list(reversed(temp)))
            else:
                ans.extend(temp)
            count = 0
        
        new_head = current = None
        for node in ans:
            node.next = None
            if not new_head:
                new_head = current = node
            else:
                current.next = node
                current = current.next
        return new_head
