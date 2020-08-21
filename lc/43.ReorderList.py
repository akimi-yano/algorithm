# 143. Reorder List

# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Example 1:

# Given 1->2->3->4, reorder it to 1->4->2->3.
# Example 2:

# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



# This does not work :

# class Solution:
#     def reorderList(self, head: ListNode) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """
#         if not head:
#             return 
#         memo = {}
#         runner = head
#         i = 0
#         while runner:
#             memo[i]= runner
#             runner= runner.next 
#             i+=1
#         # print(memo)
#         length = i 
#         half = length //2
#         # print(length)
#         i = 0
#         runner = head
#         while i<(length-1):
#             if i<(length-1-i):
#                 runner.next = memo[i]
#                 if i == half:
#                     runner.next = None
#                     break
#                 runner = runner.next
#                 runner.next = memo[length-1-i]
#                 runner = runner.next
#             i+=1


'''
If you never solved singly linked lists problems before, or you do not have a lot of experience, 
this problem can be quite difficult. However if you already know all the tricks, it is not difficult at all. 
Let us first try to understand what we need to do. For list [1,2,3,4,5,6,7] we need to return [1,7,2,6,3,5,4]. 
We can note, that it is actually two lists [1,2,3,4] and [7,6,5], where elements are interchange. So, 
to succeed we need to do the following steps:

1) Find the middle of or list - be careful, it needs to work properly both for even and for odd number of nodes. 
For this we can either just count number of elements and then divide it by to, and do two traversals of list. 
Or we can use slow/fast iterators trick, where slow moves with speed 1 and fast moves with speed 2. 
Then when fast reches the end, slow will be in the middle, as we need.

2) Reverse the second part of linked list. Again, if you never done it before, it can be quite painful, 
please read oficial solution to problem 206. Reverse Linked List. The idea is to keep three pointers: 
prev, curr, nextt stand for previous, current and next and change connections in place. 
Do not forget to use slow.next = None, in opposite case you will have list with loop.

3) Finally, we need to merge two lists, given its heads. These heads are denoted by head and prev, 
so for simplisity I created head1 and head2 variables. What we need to do now is to interchange nodes: 
we put head2 as next element of head1 and then say that head1 is now head2 and head2 is previous head1.next. 
In this way we do one step for one of the lists and rename lists, so next time we will take element from head2, 
then rename again and so on.
Complexity: Time complexity is O(n), because we first do O(n) iterations to find middle, 
then we do O(n) iterations to reverse second half and finally we do O(n) iterations to merge lists. 
Space complexity is O(1).
'''
class Solution:
    def reorderList(self, head):
        #step 1: find middle
        if not head: return 
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        #step 2: reverse second half
        prev, curr = None, slow.next
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt    
        slow.next = None
        
        #step 3: merge lists
        head1, head2 = head, prev
        while head2:
            nextt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nextt

'''
H O O O X
F N NN
S
    F N NN
 S
'''



# YAY I WROTE IT ! THIS SOLUTION WORKS AND VERY INTUITIVE !

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        fast = slow = head
        
        # step1: find middle 
        '''
        1 2 3 4 5 6
            s
                f
        
        1 2 3 4 5 
            s
                f
        '''
        # condition for odd and even 
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next

        # step2: reverse the latter half (from slow.next)
        '''
        1 2 3 4 5  
              c n
            p   
        
        '''
        prev = None 
        cur = slow.next
        slow.next = None
        
        while cur:
            nex = cur.next
            cur.next = prev 
            prev = cur 
            cur = nex
        
        tail = prev
        
        # step3: merge
        '''
        head 1 - 2
        tail 3
        
        1 - 3 - 2 
        head - 2
        tail none 
        
        '''
        while tail and head: 
            head.next, tail.next, head, tail = tail, head.next, head.next, tail.next
        
        return head 