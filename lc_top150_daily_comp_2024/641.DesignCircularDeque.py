'''
641. Design Circular Deque
Attempted
Medium
Topics
Companies
Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:

MyCircularDeque(int k) Initializes the deque with a maximum size of k.
boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
boolean isEmpty() Returns true if the deque is empty, or false otherwise.
boolean isFull() Returns true if the deque is full, or false otherwise.
 

Example 1:

Input
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 2, true, true, true, 4]

Explanation
MyCircularDeque myCircularDeque = new MyCircularDeque(3);
myCircularDeque.insertLast(1);  // return True
myCircularDeque.insertLast(2);  // return True
myCircularDeque.insertFront(3); // return True
myCircularDeque.insertFront(4); // return False, the queue is full.
myCircularDeque.getRear();      // return 2
myCircularDeque.isFull();       // return True
myCircularDeque.deleteLast();   // return True
myCircularDeque.insertFront(4); // return True
myCircularDeque.getFront();     // return 4
 

Constraints:

1 <= k <= 1000
0 <= value <= 1000
At most 2000 calls will be made to insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull.
'''

class DublyLinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularDeque:

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.cur_size = 0
        self.max_size = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.head:
            next_node = self.head
            self.head = DublyLinkedListNode(value)
            self.head.next = next_node
            next_node.prev = self.head 
        else:
            self.head = self.tail = DublyLinkedListNode(value)
        
        self.cur_size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.tail:
            prev_node = self.tail
            self.tail = DublyLinkedListNode(value)
            self.tail.prev = prev_node
            prev_node.next = self.tail
        else:
            self.head = self.tail = DublyLinkedListNode(value)

        self.cur_size += 1
        return True

    def deleteFront(self) -> bool:
        if not self.head:
            return False
        next_node = self.head.next
        self.head = next_node
        if self.head:
            self.head.prev = None
        else:
            self.tail = None

        self.cur_size -= 1
        return True

    def deleteLast(self) -> bool:
        if not self.tail:
            return False
        prev_node = self.tail.prev
        self.tail = prev_node
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        
        self.cur_size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.cur_size == 0

    def isFull(self) -> bool:
        return self.cur_size == self.max_size

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()