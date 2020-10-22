# 225. Implement Stack using Queues
# Easy

# 821

# 608

# Add to List

# Share
# Implement a last in first out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal queue (push, top, pop, and empty).

# Implement the MyStack class:

# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
# Notes:

# You must use only standard operations of a queue, which means only push to back, peek/pop from front, size, and is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue), as long as you use only a queue's standard operations.
# Follow-up: Can you implement the stack such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.

 

# Example 1:

# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]

# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False
 

# Constraints:

# 1 <= x <= 9
# At most 100 calls will be made to push, pop, top, and empty.
# All the calls to pop and top are valid.



# This solution works :


from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = deque([])
        self.queue2 = deque([])

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        
        popped = self.queue1.popleft()
        self.queue1 = self.queue2
        self.queue2 = deque([])
        return popped
    
    def top(self) -> int:
        """
        Get the top element.
        """
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
            
        topped = self.queue1[0]
        self.queue2.append(self.queue1.popleft())
        self.queue1 = self.queue2
        self.queue2 = deque([])
        return topped

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()



# This solution works !:

from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque([])

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        return self.queue.popleft()
    
    def top(self) -> int:
        """
        Get the top element.
        """
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        ans = self.queue[0]
        self.queue.append(self.queue.popleft())
        return ans

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()