# 430. Flatten a Multilevel Doubly Linked List
# Medium

# 2872

# 215

# Add to List

# Share
# You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

# Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

 

# Example 1:

# Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
# Output: [1,2,3,7,8,11,12,9,10,4,5,6]
# Explanation:

# The multilevel linked list in the input is as follows:



# After flattening the multilevel linked list it becomes:


# Example 2:

# Input: head = [1,2,null,3]
# Output: [1,3,2]
# Explanation:

# The input multilevel linked list is as follows:

#   1---2---NULL
#   |
#   3---NULL
# Example 3:

# Input: head = []
# Output: []
 

# How multilevel linked list is represented in test case:

# We use the multilevel linked list from Example 1 above:

#  1---2---3---4---5---6--NULL
#          |
#          7---8---9---10--NULL
#              |
#              11--12--NULL
# The serialization of each level is as follows:

# [1,2,3,4,5,6,null]
# [7,8,9,10,null]
# [11,12,null]
# To serialize all levels together we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:

# [1,2,3,4,5,6,null]
# [null,null,7,8,9,10,null]
# [null,11,12,null]
# Merging the serialization of each level and removing trailing nulls we obtain:

# [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
 

# Constraints:

# The number of Nodes will not exceed 1000.
# 1 <= Node.val <= 105


# This solution works:


'''
In this problem we need to traverse our multilevel doubly linked list in some special order and rebuild some connections. We can consider our list as graph, which we now need to traverse. What graph traversal algorighms do we know? We should think about dfs and bfs. Why I choose dfs? Because we need to traverse as deep as possible, before we traverse neibhour nodes, and that is what dfs do exactly! When you realise this, problem becomes much more easier. So, algorighm look like:

Put head of our list to stack and start to traverse it: pop element from it and add two two elements instead: its next and its child. The order is important: we first want to visit child and then next, that is why we put child to the top of our stack.
Each time we pop last element from stack, I write it to auxilary order list.
Last step is to rebuild from our order list flattened doubly linked list.
Complexity: time complexity is O(n), where n is number of nodes in our list. In this approach we also use O(n) additional space, because I keep order list. This can be avoid, if we make connections on the fly, but it is a bit less intuitive in my opinion, but ofcourse more optimal in space complexity.

'''
class Solution:
    def flatten(self, head):
        if not head: return head
        stack, order = [head], []

        while stack:
            last = stack.pop()
            order.append(last)
            if last.next:
                stack.append(last.next)
            if last.child:
                stack.append(last.child)
        
        for i in range(len(order) - 1):
            order[i+1].prev = order[i]
            order[i].next = order[i+1]
            order[i].child = None
            
        return order[0]
    
'''
Solution without extra array: the same idea, where we reconnect our nodes directly, without order array. It is O(h) in memory, where h is number of levels (in the worst case it will be O(n)).
'''

# class Solution(object):
#     def flatten(self, head):
#         if not head: return head
        
#         dummy = Node(0)
#         curr, stack = dummy, [head]
#         while stack:
#             last = stack.pop() 
#             if last.next:
#                 stack.append(last.next)
#             if last.child:
#                 stack.append(last.child)
#             curr.next = last
#             last.prev = curr  
#             last.child = None
#             curr = last
        
#         res = dummy.next
#         res.prev = None
#         return res


# This solution works - recusion solution:


"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def helper(node):
            start = cur = node
            prev = None
            while cur:
                nxt = cur.next
                if cur.child:
                    child_first, child_last = helper(cur.child)
                    cur.child = None
                    
                    cur.next = child_first
                    child_first.prev = cur
                    if nxt:
                        nxt.prev = child_last
                    child_last.next = nxt
                    # tricky part
                    prev = child_last
                else:
                    prev = cur
                cur = nxt
            return start, prev
                
        
        first, last = helper(head)
        return first
    
    