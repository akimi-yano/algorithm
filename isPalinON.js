# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def isPalindrome(self, head: ListNode) -> bool:
    #     runner1 = head
    #     runner2 = head
    #     check_list = []
    #     if head is None:
    #         return True
    #     if runner1.next is None:
    #         return True
    #     while runner1.next is not None:
    #         check_list.append(runner2.val)
    #         if runner1.next.next is None:
    #             break
    #         runner1 = runner1.next.next
    #         runner2 = runner2.next
    #     runner2=runner2.next
    #     while runner2.next is not None:
    #         popped = check_list.pop()
    #         if popped != runner2.val:
    #             return False
    #         runner2 = runner2.next
    #     popped = check_list.pop()
    #     if popped != runner2.val:
    #         return False
    #     if len(check_list)!=0:
    #         return False
    #     return True 

    def isPalindrome(self, head: ListNode) -> bool:
        runner1 = head
        runner2 = head
        if head is None or runner1.next is None:
            return True
        if runner1.next.next is None:
            if runner1.val != runner1.next.val:
                return False
            else:
                return True
        if runner1.next.next.next is None:
            if runner1.val != runner1.next.next.val:
                return False
            else:
                return True
        while runner1.next is not None:
            if runner1.next.next is None:
                runner1=runner1.next
                break
            runner1 = runner1.next.next
            runner2 = runner2.next
        runner2=runner2.next
        counter =0
  
        runner3=head
        
        prev = runner2
        runner2 = runner2.next
        next_node = runner2.next
        while runner2 is not None:
            runner2.next = prev
            counter +=1
            prev = runner2
            runner2 = next_node 
            if next_node is None:
                break
            else:
                next_node = next_node.next
  
        for i in range(counter+1):
            
            if runner3.val !=runner1.val:
                return False
            runner1 = runner1.next
            runner3 =runner3.next
        return True
            
            