
#!/bin/python3

import math
import os
import random
import re
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


Complete the 'isCircular' function below.
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
    runner1 = head
    runner2 = head

    while runner1 is not None or runner2 is not None or runner1.next.data !=a and runner2.next.data !=b:

        if runner1.next.data !=a :
            runner1 = runner1.next
        if runner2.next.data !=b:
            runner2 = runner2.next
    
    a_node = runner1.next
    b_node = runner2.next
    print()
    b_node.next = runner1.next.next
    runner1.next = b_node
    a_node.next = runner2.next.next
    runner2.next = a_node
    return head


#!/bin/python3

import math
import os
import random
import re
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