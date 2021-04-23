# 1825. Finding MK Average
# Hard

# 82

# 55

# Add to List

# Share
# You are given two integers, m and k, and a stream of integers. You are tasked to implement a data structure that calculates the MKAverage for the stream.

# The MKAverage can be calculated using these steps:

# If the number of the elements in the stream is less than m you should consider the MKAverage to be -1. Otherwise, copy the last m elements of the stream to a separate container.
# Remove the smallest k elements and the largest k elements from the container.
# Calculate the average value for the rest of the elements rounded down to the nearest integer.
# Implement the MKAverage class:

# MKAverage(int m, int k) Initializes the MKAverage object with an empty stream and the two integers m and k.
# void addElement(int num) Inserts a new element num into the stream.
# int calculateMKAverage() Calculates and returns the MKAverage for the current stream rounded down to the nearest integer.
 

# Example 1:

# Input
# ["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement", "calculateMKAverage", "addElement", "addElement", "addElement", "calculateMKAverage"]
# [[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]
# Output
# [null, null, null, -1, null, 3, null, null, null, 5]

# Explanation
# MKAverage obj = new MKAverage(3, 1); 
# obj.addElement(3);        // current elements are [3]
# obj.addElement(1);        // current elements are [3,1]
# obj.calculateMKAverage(); // return -1, because m = 3 and only 2 elements exist.
# obj.addElement(10);       // current elements are [3,1,10]
# obj.calculateMKAverage(); // The last 3 elements are [3,1,10].
#                           // After removing smallest and largest 1 element the container will be [3].
#                           // The average of [3] equals 3/1 = 3, return 3
# obj.addElement(5);        // current elements are [3,1,10,5]
# obj.addElement(5);        // current elements are [3,1,10,5,5]
# obj.addElement(5);        // current elements are [3,1,10,5,5,5]
# obj.calculateMKAverage(); // The last 3 elements are [5,5,5].
#                           // After removing smallest and largest 1 element the container will be [5].
#                           // The average of [5] equals 5/1 = 5, return 5
 

# Constraints:

# 3 <= m <= 105
# 1 <= k*2 < m
# 1 <= num <= 105
# At most 105 calls will be made to addElement and calculateMKAverage.


# This approach does not work - TLE:

# class MKAverage:

#     def __init__(self, m: int, k: int):
#         self.stack = []
#         self.last = []
#         self.m = m
#         self.k = k
#     def addElement(self, num: int) -> None:
#         self.stack.append(num)

#     def calculateMKAverage(self) -> int:
#         if len(self.stack) < self.m:
#             return -1
#         self.last = self.stack[-self.m:]
#         self.last.sort()
#         self.last = deque(self.last)
#         for _ in range(self.k):
#             self.last.popleft()
#             self.last.pop()
#         if not self.last:
#             return 0
#         return sum(self.last) // len(self.last)

# # Your MKAverage object will be instantiated and called as such:
# # obj = MKAverage(m, k)
# # obj.addElement(num)
# # param_2 = obj.calculateMKAverage()



# This solution works:

from sortedcontainers import SortedList
class MKAverage:
    '''
    use sorted list 
    it is a data structure to add and remove at O(logN) time 
    and can get min and max in an efficient way
    
    '''
    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.nums = deque()
        self.sorted_nums = SortedList()
        self.total = self.topk_big = self.topk_small = 0
        
    def addElement(self, num: int) -> None:
        # handle new number num
        self.total += num
        self.nums.append(num)
        idx = self.sorted_nums.bisect_left(num)
        
        # handle topksmall
        if idx < self.k:
            self.topk_small += num
            if len(self.sorted_nums) >= self.k:
                self.topk_small -= self.sorted_nums[self.k-1]
        
        # handle topkbig
        if idx >= len(self.sorted_nums) +1 - self.k:
            self.topk_big += num
            if len(self.sorted_nums) >= self.k:
                self.topk_big -= self.sorted_nums[-self.k]
        
        self.sorted_nums.add(num)
        
        # handle the num that needs to be removed from size m sliding window
        if len(self.nums) > self.m:
            num_to_remove = self.nums.popleft()
            self.total -= num_to_remove
            idx = self.sorted_nums.index(num_to_remove)
            
            if idx < self.k:
                self.topk_small -= num_to_remove
                self.topk_small += self.sorted_nums[self.k]
                
            if idx >= len(self.sorted_nums) - self.k:
                self.topk_big -= num_to_remove
                self.topk_big += self.sorted_nums[-self.k-1]
            
            self.sorted_nums.remove(num_to_remove)
        

    def calculateMKAverage(self) -> int:
        if len(self.nums) < self.m:
            return -1
        return (self.total - self.topk_small - self.topk_big) // (self.m -(2*self.k))

# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()