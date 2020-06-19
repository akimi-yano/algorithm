# 7.1 merge two sorted lists
# write a program to take two lists, assumed to be sorted, and returns their merge.
# the only field your program can change in a node is its next field.

# the two sll are sorted
# i cannot change val/ data - can only change .next  

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class SLL:
    def __init__(self):
        self.head = None
    def add_front(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return self
        else:
            new_node.next = self.head
            self.head = new_node
            return self
    def display(self):
        runner = self.head
        while runner is not None:
            print(runner.val)
            runner = runner.next
print("*"*10, "Linked List 1", "*"*10)
sl1 = SLL()
sl1.add_front(7).add_front(5).add_front(2).display()
print("*"*10, "Linked List 2", "*"*10)
sl2 = SLL()
sl2.add_front(11).add_front(3).display()

def merge_two_sll(sl1,sl2):
    r1 = sl1.head
    r2 = sl2.head
    sl3 = SLL()
    while r1 is not None and r2 is not None:
        if r1.val < r2.val:
            sl3.add_front(r1.val)
            r1=r1.next
        else:
            sl3.add_front(r2.val)
            r2=r2.next
    while r1 is not None:
        sl3.add_front(r1.val)
        r1=r1.next
    while r2 is not None:
        sl3.add_front(r2.val)
        r2=r2.next
        
    def reverse(sl3):
        prev = None
        cur = sl3.head
        while cur is not None:
            nex = cur.next
            cur.next = prev 
            prev = cur
            cur = nex
        sl3.head = prev
        return sl3.head
    reverse(sl3)    
    return sl3
sl3 = merge_two_sll(sl1,sl2)
print("*"*10, "Linked List 3", "*"*10)
sl3.display()



# more  efficient
def merge_two_sorted_lists(l1,l2):
    # create a placeholder for the result
    dummy_head = tail = Node(0)
    
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    # appends the remaining nodes of l1 or l2
    tail.next = l1 or l2
    return dummy_head.next

sl4_head_node = (merge_two_sorted_lists(sl1.head,sl2.head))

print("*"*10, "Linked List 4", "*"*10)
def printer(node):
    cur = node
    while cur is not None:
        print(cur.val)
        cur = cur.next
printer(sl4_head_node)