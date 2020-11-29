# 1669. Merge In Between Linked Lists
# Medium

# 19

# 1

# Add to List

# Share
# You are given two linked lists: list1 and list2 of sizes n and m respectively.

# Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

# The blue edges and nodes in the following figure incidate the result:


# Build the result list and return its head.

 

# Example 1:


# Input: list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
# Output: [0,1,2,1000000,1000001,1000002,5]
# Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.
# Example 2:


# Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
# Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
# Explanation: The blue edges and nodes in the above figure indicate the result.
 

# Constraints:

# 3 <= list1.length <= 104
# 1 <= a <= b < list1.length - 1
# 1 <= list2.length <= 104

# This solution works !:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        runner1 = runner2 = list1
        while b and runner2:
            runner2 = runner2.next
            b -= 1
        next_node = runner2.next
        
        while a-1 and runner1:
            runner1 = runner1.next
            a -= 1
        start_node = runner1
        
        start_node.next = list2
        
        runner3 = list2
        while runner3 and runner3.next:
            runner3 = runner3.next
        runner3.next = next_node
        return list1