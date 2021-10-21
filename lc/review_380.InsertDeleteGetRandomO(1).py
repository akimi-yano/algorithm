# 380. Insert Delete GetRandom O(1)
# Medium

# 4254

# 238

# Add to List

# Share
# Implement the RandomizedSet class:

# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.

 

# Example 1:

# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]

# Explanation
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
# randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
# randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
# randomizedSet.insert(2); // 2 was already in the set, so return false.
# randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
 

# Constraints:

# -231 <= val <= 231 - 1
# At most 2 * 105 calls will be made to insert, remove, and getRandom.
# There will be at least one element in the data structure when getRandom is called.


# This solution works:


'''
For this problem to achieve O(1) complexity for all three operation, we use 2 dictionaries: we called them direct dictionary dic_direct and inverse dictionary dic_invert.

In direct dictionary we keep indexes and corresponding values: for example: 0:3, 1:4, 2:1 means, that we have 3 values in our dictionary: [3,4,1].
In invert dictionary we keep the opposite correspondences: 3:0, 4:1, 1:2. Why we need to keep two dictionaries? Because we want to search quickly both by keys and by values.
num_elem is to count number of elements in our set (you can avoid it, but code becomes a bit more readible).
Insert. When we do insert, we first check if element is already in our invert dictionary, because we are looking for value. We do it in O(1). If element is not here, we just add it to the "end" of our dictionaries, by this I mean, we add it with biggest existing index in dicionary, increased by 1. For example if we want to add new element 10 into 0:3, 1:4, 2:1, then we have 0:3, 1:4, 2:1, 3:10.

Remove: this one is a bit more complicated. Imagine, that we want to remove element 4 from 0:3, 1:4, 2:1, 3:10. What we need to do in this case? We find it and delete first, but now we have gap in our indexes: 0:3, 2:1, 3:10. We can easily fix it, let us take the last element and put it into our gap, so we have 0:3, 1:10, 2:1 now. If we do not have gap, that is we removed the last element, then we do not need to do this action. In any case we have O(1) complexity.

getRandom This one is easy, we just generate random number, uniformly distributed between 0 and 1, multiply it by number of all elements in set and evaluate floor function. For example if we have 5 elements, and we generated number 0.7, then we need to choose element number 3. Complexity is O(1).
'''
class RandomizedSet:
    def __init__(self):
        self.dic_direct = {}
        self.dic_invert = {}
        self.num_elem = 0
        
    def insert(self, val: int) -> bool:
        if val in self.dic_invert:
            return False
        else:
            self.dic_invert[val] = self.num_elem
            self.dic_direct[self.num_elem] = val
            self.num_elem += 1
            return True
        
    def remove(self, val):
        if val not in self.dic_invert:
            return False
        else:
            ind = self.dic_invert.pop(val)
            self.dic_direct.pop(ind)
            if ind != self.num_elem - 1:
                self.dic_direct[ind] = self.dic_direct[self.num_elem - 1]
                self.dic_invert[self.dic_direct[self.num_elem - 1]] = ind
                self.dic_direct.pop(self.num_elem - 1)
            self.num_elem -= 1
            return True
        
    def getRandom(self):
        index = floor(random.random()*self.num_elem)
        return self.dic_direct[index]
