# 1286. Iterator for Combination
# Medium

# 787

# 60

# Add to List

# Share
# Design the CombinationIterator class:

# CombinationIterator(string characters, int combinationLength) Initializes the object with a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
# next() Returns the next combination of length combinationLength in lexicographical order.
# hasNext() Returns true if and only if there exists a next combination.
 

# Example 1:

# Input
# ["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
# [["abc", 2], [], [], [], [], [], []]
# Output
# [null, "ab", true, "ac", true, "bc", false]

# Explanation
# CombinationIterator itr = new CombinationIterator("abc", 2);
# itr.next();    // return "ab"
# itr.hasNext(); // return True
# itr.next();    // return "ac"
# itr.hasNext(); // return True
# itr.next();    // return "bc"
# itr.hasNext(); // return False
 

# Constraints:

# 1 <= combinationLength <= characters.length <= 15
# All the characters of characters are unique.
# At most 104 calls will be made to next and hasNext.
# It's guaranteed that all calls of the function next are valid.


# This solution works:


from itertools import combinations
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.all = list(sorted(combinations(characters, combinationLength), reverse = True))

    def next(self) -> str:
        return "".join(self.all.pop())

    def hasNext(self) -> bool:
        return len(self.all) > 0


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()



# This solution works:


from collections import deque
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        # store all the unique options in self.storage   
        self.queue = deque([]) # ['ab','ac','bc'] # populate the list with combinationLength using recursion
        self.chars = characters
        self.comb_len = combinationLength
        self.helper('', 0)
        
    def helper(self, s, start):
        if len(s) == self.comb_len:
            self.queue.append(s)
            return 
        for i in range(start, len(self.chars)):
            self.helper(s + self.chars[i], i+1)
        
    def next(self) -> str:
        return self.queue.popleft()

    def hasNext(self) -> bool:
        return self.queue


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()