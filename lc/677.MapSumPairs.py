# 677. Map Sum Pairs
# Medium

# 890

# 106

# Add to List

# Share
# Implement the MapSum class:

# MapSum() Initializes the MapSum object.
# void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, the original key-value pair will be overridden to the new one.
# int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.
 

# Example 1:

# Input
# ["MapSum", "insert", "sum", "insert", "sum"]
# [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
# Output
# [null, null, 3, null, 5]

# Explanation
# MapSum mapSum = new MapSum();
# mapSum.insert("apple", 3);  
# mapSum.sum("ap");           // return 3 (apple = 3)
# mapSum.insert("app", 2);    
# mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)
 

# Constraints:

# 1 <= key.length, prefix.length <= 50
# key and prefix consist of only lowercase English letters.
# 1 <= val <= 1000
# At most 50 calls will be made to insert and sum.

# This solution works: - Trie solution

class TrieNode:
    def __init__(self, char = None):
        self.val = 0
        self.char = char
        self.next = {}

class MapSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        for c in key:
            if c not in cur.next:
                cur.next[c] = TrieNode(c)
            cur = cur.next[c]
        cur.val = val
    
    def helper(self, cur):
        total = 0
        total+= cur.val
        for next_char in cur.next:
            total += self.helper(cur.next[next_char])
        return total
    
    def sum(self, prefix: str) -> int:
        cur = self.root
        for c in prefix:
            if c in cur.next:
                cur = cur.next[c]
            else:
                return 0
        return self.helper(cur)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)