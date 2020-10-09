'''
https://leetcode.com/problems/reorder-list/


143. Reorder List
Medium

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''

"""
1. two pointers, one for first, one for the second half
    a. have a fast slow pointer, when fast reaches the end, slow is head of second half list
2. reverse second half
    a. two pointers, one for the prev, one for cur, save cur.next, change cur.next to prev
3. interleve the two lists
    a. going through both lists evenly, adding one then the other

1 -> 2 -> 3
5 -> 4
    |

1 -> 5 -> 2 -> 4 -> 3 -> None


    1 -> 2 -> 3 -> 4
         |.   |.   |
      pre_n  node.  next_n
      
      

"""

def find_middle(head):
    if head is None:
        return None

    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        
    return slow

def reverse_linked_list(head):
    pre_n = None
    node = head
    while node is not None:
        next_n = node.next
        node.next = pre_n
        pre_n = node
        node = next_n
        
    return pre_n
        

def reorderList(self, head: ListNode) -> None:
    if head is None:
        return

    head1 = head
    head2 = find_middle(head)
    head2 = reverse_linked_list(head2)
    node1 = head1
    node2 = head2
    while node2.next is not None:
        tmp1 = node1.next
        tmp2 = node2.next
        node1.next = node2
        node2.next = tmp1
        node1 = tmp1
        node2 = tmp2
        
        
class Solution:
    
#         7-2-3+3+1-5 = 1
#         point <= 0: die
#         minimum sum to travel from bottom right corner to [0][0]
#        
#         brute force: dfs or bfs
#         dynamic programming: only right and down
   
    # Time O(MN) Space O(N), runtime = 72 ms
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        if not dungeon or not dungeon[0]: return dungeon
        
        size = len(dungeon)
        col_size = len(dungeon[0])
        dp = [float(inf)] * (col_size + 1)
        dp[col_size] = 1
        dp[col_size-1] = 1
        for i in range(size-1, -1, -1):
            dp[col_size] = dp[col_size-1]
            for j in range(col_size-1, -1, -1):
                dp[j] = max(1, min(dp[j+1], dp[j])- dungeon[i][j])    
                
        return dp[0]


    
    
    
    

    # Time O(MN) Space O(1), runtime = 76 ms
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        if not dungeon or not dungeon[0]: return dungeon
        
        size = len(dungeon)
        col_size = len(dungeon[0])   
        dungeon[size-1][col_size-1] = max(1, dungeon[size-1][col_size-1] * (-1) + 1)

        for j in range(col_size-2, -1, -1):
            dungeon[size-1][j] = max(1, dungeon[size-1][j+1] - dungeon[size-1][j])
        for i in range(size-2, -1, -1):
            dungeon[i][col_size-1] = max(1, dungeon[i+1][col_size-1] - dungeon[i][col_size-1])
        for i in range(size-2, -1, -1):
            for j in range(col_size-2, -1, -1):
                dungeon[i][j] = max(1, min(dungeon[i+1][j]-dungeon[i][j], dungeon[i][j+1]-dungeon[i][j]))

        return dungeon[0][0]

    
    
    
        
        
        
        
    




























'''
876. Middle of the Linked List
Easy

Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Note:

The number of nodes in the given list will be between 1 and 100.
'''

1 -> 2
|    |

def middle_of_linked_list(head):
    if head is None:
        return None

    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        
    return slow
        
    # target = length // 2
    # node = head
    # while target > 0:
    #     target -= 1
    #     node = node.next
        
    # return node
    