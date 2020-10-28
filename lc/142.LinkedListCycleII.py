# 142. Linked List Cycle II
# Medium

# 3290

# 254

# Add to List

# Share
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Notice that you should not modify the linked list.

# Follow up:

# Can you solve it using O(1) (i.e. constant) memory?


# Example 1:


# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.
# Example 2:


# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the first node.
# Example 3:


# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.


# Constraints:

# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.


# This solution works !

'''
Time: O(N)
Space: O(N)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        seen = set([])
        cur = head

        while cur:
            if cur in seen:
                return cur
            seen.add(cur)

            cur = cur.next
        return None
    
    
# Optimization - 
'''
Time: O(N)
Space: O(1)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None

        slower = faster = head
        # find out if there is cycle
        while faster and faster.next:
            slower = slower.next
            faster = faster.next.next
            # check after moving pointers 
            if slower == faster:
                break
        else:
            # return None if there is no cycle - if the while condition turns False to get out of the loop instead of "break"
            return None
        
        # check from the beginning to find the intersection to return - move at the same speed from head
        intersect = slower
        cur = head
        while cur != intersect:
            cur = cur.next
            intersect = intersect.next
        return intersect
        
        
        
'''
math proof of why this approach works

                          _____
                         /     \  Ln
        head____________answer  \
                        \       /
                H        X_____/   D

        H: distance between head and answer node (which is the beginning of the intersection)
        X: the intersection of the slow and fast pointers
        Ln: L is the length of the cycle and n is the # of turns you made in the cycle
        D: distance inside of L which is from L to X
        Ln-D: distance between X and answer
        
        H+D: # of blocks slower node moved
        2 * (H+D): # of blocks faster node moved
        
        H+D+L*n = 2 *(H+D)
        L*n = 2H + 2D -H -D
        L*n = H + D
        H = L*n - D
        
        That is why by moving the slow pointer and new pointer from beginning, we can get to the same node which is answer!
'''