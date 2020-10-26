# 21. Merge Two Sorted Lists
# Easy

# 5192

# 657

# Add to List

# Share
# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

 

# Example 1:


# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: l1 = [], l2 = []
# Output: []
# Example 3:

# Input: l1 = [], l2 = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both l1 and l2 are sorted in non-decreasing order.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        input:
        l1 - ListNode that is head = beginning
        1 -> 2 -> 4
        l2 - ListNode that is head = beginning
        1 -> 3 -> 4
        
        output:
        1 -> 1 -> 2 -> 3 -> 4 -> 4 -> X
        

    # iterative approach -  
        l1 l2   
        x   x   return x
        x       return l2
            x   return l1
                ->  merge two sorted linked list
                1 decide a head by comparing the 2 head - smaller one is head
                - if its the same then either is fine
                2 iterate through both linked lists and keep building the answer list 
                on top of the head by choosing smaller nodes in value
                3 return head
    
    # recursive approach - 

    in recursion pass in c1 and c2
    
    if not c1 - return c2
    if not c2 - return c1
    
    compare c1.val and c2.val
    if c1.val < c2.val:
        c1.next =   next scope c1.next vs c2
    return c1
    else:
        c2.next =  next scope c1 vs c2.next
    return c2
        '''

# iterative approach
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1

        head = None
        merged_cur = None
        while l1 and l2:
            if l2.val < l1.val:
                l1, l2 = l2, l1
            if head is None:
                head = l1
            else:
                merged_cur.next = l1
            merged_cur, l1 = l1, l1.next
        
        if l1:
            merged_cur.next = l1
        if l2:
            merged_cur.next = l2
        return head
            
        
# recursive approach 
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        def helper(c1, c2):
            if not c1:
                return c2
            elif not c2:
                return c1
            
            if c1.val < c2.val:
                c1.next = helper(c1.next, c2)
                return c1
            else:
                c2.next = helper(c1, c2.next)
                return c2

        return helper(l1, l2)
        
        
        
        