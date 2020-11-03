# 147. Insertion Sort List
# Medium

# 791

# 627

# Add to List

# Share
# Sort a linked list using insertion sort.


# A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
# With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

# Algorithm of Insertion Sort:

# Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
# It repeats until no input elements remain.

# Example 1:

# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:

# Input: -1->5->3->4->0
# Output: -1->0->3->4->5

# This solution works ! - there should be a better ways though! 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        cur = head
        val_arr = []
        while cur:
            val_arr.append(cur.val)
            cur= cur.next
        val_arr.sort()     
        new_head = ListNode(val_arr[0])
        cur = new_head
        i = 1
        while i < len(val_arr):
            cur.next = ListNode(val_arr[i])
            cur = cur.next
            i += 1
        return new_head
            
            
# This solution works !

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)
        new_cur = dummy
        cur = head
        while cur:
            node = cur
            head = cur.next
            new_cur = dummy
            while new_cur and new_cur.next and new_cur.next.val <= node.val:
                new_cur = new_cur.next
            next_node = new_cur.next
            new_cur.next = node
            node.next = next_node
            
            cur = head
            
        return dummy.next