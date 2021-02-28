# 895. Maximum Frequency Stack
# Hard

# 1587

# 34

# Add to List

# Share
# Implement FreqStack, a class which simulates the operation of a stack-like data structure.

# FreqStack has two functions:

# push(int x), which pushes an integer x onto the stack.
# pop(), which removes and returns the most frequent element in the stack.
# If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.
 

# Example 1:

# Input: 
# ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
# [[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
# Output: [null,null,null,null,null,null,null,5,7,5,4]
# Explanation:
# After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:

# pop() -> returns 5, as 5 is the most frequent.
# The stack becomes [5,7,5,7,4].

# pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
# The stack becomes [5,7,5,4].

# pop() -> returns 5.
# The stack becomes [5,7,4].

# pop() -> returns 4.
# The stack becomes [5,7].
 

# Note:

# Calls to FreqStack.push(int x) will be such that 0 <= x <= 10^9.
# It is guaranteed that FreqStack.pop() won't be called if the stack has zero elements.
# The total number of FreqStack.push calls will not exceed 10000 in a single test case.
# The total number of FreqStack.pop calls will not exceed 10000 in a single test case.
# The total number of FreqStack.push and FreqStack.pop calls will not exceed 150000 across all test cases.

# This solution works:
'''
sorted list + dictionary
'''

from sortedcontainers import SortedList
class FreqStack:

    def __init__(self):
        self.nums = SortedList()
        self.order = 0
        self.memo = {}
        
    def push(self, x: int) -> None:
        if x not in self.memo:
            self.memo[x]  = []
        else:
            last_freq = len(self.memo[x])
            last_order = self.memo[x][-1]
            self.nums.remove((last_freq, last_order, x))
            
        self.memo[x].append(self.order)
        new_freq = len(self.memo[x])
        new_order = self.order
        self.order += 1
    
        self.nums.add((new_freq, new_order, x))
        
    def pop(self) -> int:
        cur_freq, cur_order, val = self.nums.pop()
        
        self.memo[val].pop()
        new_freq = len(self.memo[val])
        if new_freq > 0:
            new_order = self.memo[val][-1]
            self.nums.add((new_freq, new_order, val))
        else:
            del self.memo[val]
        
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()