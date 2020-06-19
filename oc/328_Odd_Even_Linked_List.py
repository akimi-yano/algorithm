# 328. Odd Even Linked List

'''
Given a singly linked list, group all odd nodes together 
followed by the even nodes. 
Please note here we are talking about the node number and 
not the value in the nodes.

You should try to do it in place. The program should run in O(1) 
space complexity and O(nodes) time complexity.

Time O(N) Space O(1)

Example 1:
index. 1  2. 3. 4. 5
Input: 1->2->3->4->5->NULL
        1. 3. 5. 2  4 
Output: 1->3->5->2->4->NULL
Example 2:
       1  2. 3. 4. 5
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
'''
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
ex1)
 1  2  3  4  5
[1][2][3][4][5]
odd -> even
1 3 5 2 4 none

ex2)
 2  1  3  5  6  4  7
[1][2][3][4][5][6][7]   
2   3  6  7  1  5  4
[1][3][5][7][2][4][6]

possible edge case:
head node could be none

0<len<10,000

return head node 

Time O(N) Space O(1)

1 - check which one is odd and even - 
    temp_odd - first node - tail 
    temp_even - second node 
2 merge the 2 temp ones and return head

      head ---> 
      result_head = odd
      even_head = even

    connect temp odd tail and head of the temp even 
    
'''
# incomplete code 

# def oddEvenList(self, head: ListNode) -> ListNode:
    
#     if head is None:
#       return None
  
#     temp_odd = odd_tail = head
#     temp_even = even_tail = head.next
    
    # result_head = odd.  ----> return
    # even_head = even.   ---> join
    
    # runner = head.next.next
    # counter = 3
    
    # while runner is not None:
    #   if counter%2!=0:
    #     odd_tail.next = runner
    #     odd_tail = odd_tail.next
    #   else:
    #     even_tail.next = runner
    #     even_tail = even_tail.next  
    #   runner = runner.next
    
    # solution that works !
def oddEvenList(self, head: ListNode) -> ListNode:
        
    if not head: 
        return None
        
    odd = head
    even = head.next
        
    result_head = odd
    even_head = even
        
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
        
    odd.next = even_head
    return result_head
# print(oddEvenList())






