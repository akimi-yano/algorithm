# 1286. Iterator for Combination

# Design an Iterator class, which has:

# A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
# A function next() that returns the next combination of length combinationLength in lexicographical order.
# A function hasNext() that returns True if and only if there exists a next combination.
 

# Example:

# CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

# iterator.next(); // returns "ab"
# iterator.hasNext(); // returns true
# iterator.next(); // returns "ac"
# iterator.hasNext(); // returns true
# iterator.next(); // returns "bc"
# iterator.hasNext(); // returns false
 

# Constraints:

# 1 <= combinationLength <= characters.length <= 15
# There will be at most 10^4 function calls per test.
# It's guaranteed that all calls of the function next are valid.


# This solution works and it is intuitive to me - but there might be better ways to solve this 

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        # store all the unique options in self.storage   
        self.storage = [] # ['ab','ac','bc'] # populate the list with combinationLength using recursion
        self.chars = characters
        self.comb_len = combinationLength
        self.cur = 0
        self.helper('', 0, self.comb_len, self.storage,0)
        
    def helper(self, s, start, target, res, count):
        if count == target:
            res.append(s)
            return 
        for i in range(start, len(self.chars)):
            self.helper(s + self.chars[i], i+1, target, res, count+1)
        
    def next(self) -> str:
        self.cur += 1
        return self.storage[self.cur - 1]

    def hasNext(self) -> bool:
        return self.cur < len(self.storage) 


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()