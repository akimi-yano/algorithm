# WEEK2 Exam Probelms (2 problems)
import math
# Problem 1. Condensed List 
# Given a list of integers, remove any nodes that have values that have previously occurred in the list and return a reference to the head of the list.

# Complete the function condense in the editor below. 

# The function must return a reference to a LinkedListNode, the first node of a list that contains only the unique value nodes from the original list, in order.

# condense has the following parameter(s):

#     head:  the head of a singly-linked list of integers, a LinkedListNode

# Note:. A LinkedListNode has two attributes: data, an integer, 
# and next, a reference to the next item in the list or the language equivalent of null at the tail.

# Constraints

# 1 ≤ n ≤ 105
# 0 ≤ LinkedListNode[i].data ≤ 1000

# example:
    
# -input linked list with dups
# 8
# 3
# 4
# 3
# 2
# 6
# 1
# 2
# 6

# -output linked list without dups
# 3
# 4
# 2
# 6
# 1



# Complete the 'condense' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST head as parameter.



# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next


def condense(head):
    if head is None:
        return head
    runner = head
    visited = set([])
    visited.add(runner.data)
    while runner is not None and runner.next is not None:
        if runner.next.data not in visited:
            visited.add(runner.next.data)
            runner = runner.next
        else:
            runner.next = runner.next.next

    return head




# Problem 2. Check the Structure

# A binary tree uses a multi-node data structure where each node may have 0 to 2 child nodes, 
# and has one stored value, its node number in this case. A tree may either be:

# An empty tree, the root is null.
# A non-empty tree with a non-null root node that contains a value and up to 2 subtrees, left and right, which are also binary trees.


# A binary tree is classified as a binary search tree (BST) if all of the non-null nodes exhibit two properties:

# The left subtree of each node contains only nodes with values that are lower than its own value.
# The right subtree of each node contains only nodes with values that are higher than its own value.


# A pre-order traversal is a recursive tree traversal method where the current node is visited first, 
# then the left subtree, and then the right subtree. The following pseudocode parses a tree into a list using pre-order traversal:

# If the root is null, return the null list.
# For a non-null root node:
# Create a pre-order traversal list, left, of the left subtree.
# Create a pre-order traversal list, right, of the right subtree.
# Return the concatenated list: the non-null node + left + right.


# Determine whether a traversal history can describe a path for a valid BST. 
# Given a traversal history of one or many binary trees, check whether each path represents a valid BST or not. 
# Return a string, one for each test. Answer YES if the path can represent a valid BST, or NO if it cannot.

# Example

# nodes = [2, 1, 3, 4, 5]



# The root node will always be the first node in the array. In this case, the root is at node 2
# Next 1 is less than 2. Place the node 1 at the left of node 2.
# Next 3 is greater than 2. Place the node 3 at the right of node 2.
# Next 4 is greater than 3. Place the node 4 at the right of node 3.
# Next 5 is greater than 4. Place the node 5 at the right of node 4.
# This graph meets the definition of a BST.

# Function Description 



# Complete the isValid function below.



# isValid has the following parameter:

#     int a[n]: An array of integers, the values in the order encountered in the traversal of the tree.

# Returns:

#     string[n]: for each test, either the string YES if the path represents a valid BST, or NO otherwise.



# Constraints

# 1 ≤ q ≤ 10
# 1 ≤ n, a[i] ≤ 100


# Input Format
# Sample Case 0
# Sample Input 0

# STDIN          Function
# -----          --------

# 3              →   a[] size n = 3 (query 0)
# 1 3 2          →   a = [1, 3, 2]

# 3              →   a[] size n = 3 (query 1)
# 2 1 3          →   a = [2, 1, 3]

# 6              →   a[] size n = 6 (query 2)
# 3 2 1 5 4 6    →   a = [3, 2, 1, 5, 4, 6]

# 4              →   a[] size n = 4 (query 3)
# 1 3 4 2        →   a = [1, 3, 4, 2]

# 5              →   a[] size n = 5 (query 4)
# 3 4 5 1 2      →   a = [3, 4, 5, 1, 2]

# output: 
# YES
# YES
# YES
# NO
# NO



# Diagram (a) is valid, so return the string YES.
# Diagram (b) is valid, so return the string YES.
# Diagram (c) is valid, so return the string YES.
# Diagram (d), the query 1 3 4 2, is not valid. The root is 1 because it is the first value in the list. The second value of 3 must be the right child of 1 because it is greater. Likewise, the third value, 4, must be the right child of 3. For 2 to be the last value in the traversal, it has to be the left child of 4. It is less than the root value 3 above it and is on its right subtree. Return the string NO.
# Diagram (e), the query 3 4 5 1 2, is not valid. The root, the first value in the list, is 3.  The second value, 4,  must be the right child of 3. The third value, 5, must be the right child of 4. For the fourth value to be 1, it must be the left child of 5, but that is less than the root at 4 and is in its right subtree.  Return the string NO.


# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY a as parameter.
#

def isValidBST(a):
    leaf_nodes = []
    leaf_nodes.append((a[0],math.inf))
    leaf_nodes.append((-math.inf,a[0]))
    for i in range(1,len(a)):
        while True:
            # print(leaf_nodes, a[i])
            if len(leaf_nodes)<1:
                return "NO"
            node = leaf_nodes.pop()
            lower, upper = node
            if a[i] >= lower and a[i] <= upper:
                leaf_nodes.append((a[i],upper))
                leaf_nodes.append((lower,a[i]))
                break
            else:
                pass
    return "YES"
    
print(isValidBST([2, 1, 3, 4, 5])) 
print(isValidBST([1, 3, 2]))
print(isValidBST([2, 1, 3]))
print(isValidBST([3, 2, 1, 5, 4, 6]))
print(isValidBST([1, 3, 4, 2]))
print(isValidBST([3, 4, 5, 1, 2]))

# Expected outputs:
# YES
# YES
# YES
# YES
# NO
# NO