# 284. Peeking Iterator
# Medium

# 711

# 503

# Add to List

# Share
# Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().

# Example:

# Assume that the iterator is initialized to the beginning of the list: [1,2,3].

# Call next() gets you 1, the first element in the list.
# Now you call peek() and it returns 2, the next element. Calling next() after that still return 2. 
# You call next() the final time and it returns 3, the last element. 
# Calling hasNext() after that should return false.
# Follow up: How would you extend your design to be generic and work with all types, not just integer?





# This solution works : after optimization

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.cur = None
        self.it = iterator
        if self.it.hasNext():
            self.cur = self.it.next()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.cur
        
    def next(self):
        """
        :rtype: int
        """
        nxt = None
        if self.it.hasNext():
            nxt = self.it.next()
        return_value = self.cur
        self.cur = nxt
        return return_value
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cur is not None

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].





# This solution works : before optimization

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.arr = []
        self.i = 0
        while iterator.hasNext():
            self.arr.append(iterator.next())

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.hasNext():
            return self.arr[self.i]
        
    def next(self):
        """
        :rtype: int
        """
        # return next(self.iterator)
        if self.hasNext():
            val =  self.arr[self.i]
            self.i += 1
            return val

    def hasNext(self):
        """
        :rtype: bool
        """
        
        return self.i < len(self.arr)

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].