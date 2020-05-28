import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


#
# Complete the 'swapNodes' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST head
#  2. INTEGER a
#  3. INTEGER b
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next


# Complete the 'isCircular' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts INTEGER_SINGLY_LINKED_LIST node as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def swapNodes(head, a, b):
    # take care of pre_a, a_node
    a_node = None
    pre_a = head
    if head.data == a:
        a_node = head
        pre_a = None
    while a_node is None and pre_a.next is not None:
        if pre_a.next.data == a:
            a_node = pre_a.next
            break
        pre_a = pre_a.next

    # take care of pre_b, b_node
    b_node = None
    pre_b = head
    if head.data == b:
        b_node = head
        pre_b = None
    while b_node is None and pre_b.next is not None:
        if pre_b.next.data == b:
            b_node = pre_b.next
            break
        pre_b = pre_b.next
    
    # if a or b was not found
    if a_node is None or b_node is None:
        return head
    
    # if a and b are the same
    if a_node is b_node:
        return head
    
    # swap a_node.next, b_node.next
    a_node.next, b_node.next = b_node.next, a_node.next
    
    # if a_node is head, then only pre_b needs to be changed (pre_a doesn't exist)
    if a_node is head:
        pre_b.next = a_node
        return b_node
    # if b_node is head, then only pre_a needs to be changed (pre_b doesn't exist)
    if b_node is head:
        pre_a.next = b_node
        return a_node
    # else, swap pre_a.next and pre_b.next
    pre_a.next, pre_b.next = pre_b.next, pre_a.next
    return head

linked_list = SinglyLinkedList()
linked_list.insert_node(1)
linked_list.insert_node(2)
linked_list.insert_node(3)
linked_list.insert_node(4)
linked_list.insert_node(5)
print_singly_linked_list(linked_list.head, ' ',sys.stdout)
linked_list.head = swapNodes(linked_list.head, 5, 1)
print("*"*20)
print_singly_linked_list(linked_list.head, ' ',sys.stdout)



#
# Complete the 'reverseLinkedList' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST node as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def reverseLinkedList(node):
    prev = None
    current = node
    while current is not None:
        nextnode = current.next
        current.next = prev
        prev = current 
        current = nextnode
    return prev