# 1721. Swapping Nodes in a Linked List
# Medium

# 372

# 26

# Add to List

# Share
# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
# Output: [7,9,6,6,8,7,3,0,9,5]
# Example 3:

# Input: head = [1], k = 1
# Output: [1]
# Example 4:

# Input: head = [1,2], k = 1
# Output: [2,1]
# Example 5:

# Input: head = [1,2,3], k = 2
# Output: [1,2,3]
 

# Constraints:

# The number of nodes in the list is n.
# 1 <= k <= n <= 105
# 0 <= Node.val <= 100


# This solution works - but did not need to swap nodes just swap values :

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        newhead = ListNode(None)
        newhead.next = head
        
        slow = fast = newhead
        prev = None
        for _ in range(k):
            if fast:
                prev = fast
                fast = fast.next
        node1_prev = prev
        
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        node2_prev = slow
        
        node1 = node1_prev.next
        node2 = node2_prev.next
        node1_next = node1.next
        node2_next = node2.next
        # print(node1_prev, node2_prev, node1, node2)
        
        if node1_prev is not node2:
            node1_prev.next = node2
        
        if node1 is not node2_next:
            node1.next = node2_next
        else:
            node1.next = node2
        
        if node1 is not node2_prev:
            node2_prev.next = node1
            node2.next = node1_next
        else:
            node2.next = node1
            
        return newhead.next
        '''
        100
        None
        90 
        100
        p2 p1,n2 n1
        [x, 100, 90]
        2
        100 -> 100
        90->90
        
        x-> 90
        100->x
        
        p1 n1 p2 n2
        1 (2) 3 (4) 5
        
        1->4 
        2->5
        
        3->2
        4->3
        
        
        1 (4) 3 (2) 5
        
           p2
        p1 n1 n2
        x  1  2
        
        x->2
        1->x
        
           p2
        p1 n1 n2
        x  1  2
        
        x-> 2 -> 2
        1->1->x
        x  2  1
        


        '''

# This solution works - optimization - just swapping values, not the nodes:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:

        cur = head
        length = 0
        while cur:
            cur = cur.next
            length +=1
        from_head = k
        from_tail = length - (k-1)
        first = second = head

        count = 1
        while count < length:
            if count < from_head:
                first = first.next
            if count < from_tail:
                second = second.next
            count += 1

        second.val, first.val = first.val, second.val

        return head
            
            
                