# 92. Reverse Linked List II
# Medium

# 3386

# 173

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

# This approach does not work:

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
#         if m == n:
#             return head
#         '''
#         1   2   3   4   5
#             -   -   -       
#         tail = end.next.next
#         start.next = reverse_list(start.next, end.next)
#         start.next.next = tail
#         '''
        
#         def reverse_list(node1, node2):
#             cur = node1
#             prev = dummy = ListNode(None)
#             while cur != node2:
#                 nextnode = cur.next
#                 cur.next = prev
#                 prev = cur
#                 cur = nextnode
#             return prev, node1
#         '''
#         2   3   4
#         n1      n2
#      p  cur n   n
#         p   c
#             p   c
#         '''
                
#         swaphead = False

#         cur = head
#         start = cur
#         if m <= cur.val <= n:
#             swaphead = True
#         else:
#             while cur and cur.next:
#                 if m <= cur.next.val <= n:
#                     start = cur
#                     break
#                 cur = cur.next

#         end = cur
#         while cur and cur.next:
#             if not (m <= cur.next.val <= n):
#                 end = cur
#                 break
#             cur = cur.next
        
#         tail = end.next
#         if swaphead:
#             head, newtail = reverse_list(head, end.next)
#         else:
#             start.next, newtail = reverse_list(start.next, end.next)
#         newtail.next = tail
        
#         return head



# This solution works:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        
        def reverse_list(node1, node2):
            cur = node1
            prev = dummy = ListNode(None)
            while cur != node2:
                nextnode = cur.next
                cur.next = prev
                prev = cur
                cur = nextnode
            return prev, node1
                
        swaphead = False

        cur = head
        start = cur
        if m == 1:
            swaphead = True
        else:
            while m > 2:
                cur = cur.next
                m -= 1
                n -= 1
            start = cur

        while n > 1:
            cur = cur.next
            n -= 1
        end = cur
        
        tail = end.next
        if swaphead:
            head, newtail = reverse_list(head, end.next)
        else:
            start.next, newtail = reverse_list(start.next, end.next)
        newtail.next = tail
        
        return head
    
    
# This solution works:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        def helper(node, count):
            p = None
            c = node
            while count:
                temp = c.next
                c.next = p
                p, c = c, temp
                count -= 1
            node.next = c
            return p
        
        if m == n:
            return head
        
        dummy = ListNode(val=None, next=head)
        
        idx = 1
        prev = dummy
        cur = head
        while idx < m:
            prev, cur = cur, cur.next
            idx += 1
        num = n - m + 1
        prev.next = helper(cur, num)
        
        return dummy.next