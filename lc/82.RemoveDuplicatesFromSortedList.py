# 82. Remove Duplicates from Sorted List II
# Medium

# 2477

# 121

# Add to List

# Share
# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

# Example 1:


# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]
# Example 2:


# Input: head = [1,1,1,2,3]
# Output: [2,3]
 

# Constraints:

# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.

# This solution works !

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import Counter
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        counts = Counter()
        cur = head
        while cur:
            counts[cur.val] += 1
            cur = cur.next
        counts_arr = list(counts.items())
        for k, v in counts_arr:
            if v <= 1:
                del counts[k]
        cur = head
        new_head = None
        while cur:
            if cur.val in counts:
                pass
            else:
                if not new_head:
                    new_head = ListNode(cur.val)
                    new_cur = new_head
                else:
                    new_cur.next = ListNode(cur.val)
                    new_cur = new_cur.next
    
            cur = cur.next
        return new_head

# This solution works !

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(float('inf'), head)
        prev, cur = dummy, head 
        while cur:
            if cur.next and cur.val == cur.next.val:
                # duplicates - delete them
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                # move one more time
                cur = cur.next
                prev.next = cur
            else:
                prev, cur = cur, cur.next
        return dummy.next
    
# This approach does not work
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         if not head:
#             return 
#         head_to_return = ListNode(float('inf'))
#         cur_to_add = head_to_return
#         cur = head
#         prev = head_to_return
#         dup = False
        
#         while cur:
#             if cur.val != prev.val:
#                 if not dup:
#                     cur_to_add.next = prev
#                     cur_to_add = cur_to_add.next
#                 else:
#                     dup = False
#             else:
#                 dup = True
#             prev = cur
#             cur = cur.next
#             prev.next = None

#         if prev and not dup:
#             prev.next = None
#             cur_to_add.next = prev
#             cur_to_add = cur_to_add.next

#         return head_to_return.next
            


# This approach does not work
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# from collections import Counter
# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         counts = Counter()
#         cur = head
#         while cur:
#             counts[cur.val] += 1
#             cur = cur.next
#         counts_arr = list(counts.items())
#         for k, v in counts_arr:
#             if v <= 1:
#                 del counts[k]
#         cur = head
#         new_head = None
#         while cur:
#             if cur in counts:
#                 pass
#             else:
#                 if not new_head:
                    
#                     new_head = cur
#                     new_cur = new_head
#                 else:
#                     new_cur.next = cur
#                     new_cur = new_cur.next
                
#             cur = cur.next
#         return new_head