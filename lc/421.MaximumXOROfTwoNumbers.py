# 421. Maximum XOR of Two Numbers in an Array
# Medium

# 1455

# 182

# Add to List

# Share
# Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

# Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

# Could you do this in O(n) runtime?

# Example:

# Input: [3, 10, 5, 25, 2, 8]

# Output: 28

# Explanation: The maximum result is 5 ^ 25 = 28.




# THIS APPROACH DOES NOT WORK: (TLED)

# class Solution:
#     def findMaximumXOR(self, nums: List[int]) -> int:
#         best = 0
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if i == j:
#                     continue
#                 best = max(best, nums[i] ^ nums[j])
#         return best


# THIS APPROACH WORKS:
# trie (binary tree has zero and one children)

class TrieNode():
    def __init__(self):
        self.one = None
        self.zero = None

class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        root = TrieNode()
        for num in nums:
            node = root
            for j in range (31, -1, -1):
                tmp = num & 1 << j
                if tmp:
                    if not node.one:
                        node.one = TrieNode()
                    node = node.one
                else:
                    if not node.zero:
                        node.zero = TrieNode()
                    node = node.zero
                    
        ans = 0
        for num in nums:
            node = root
            tmp_val = 0
            for j in range (31, -1, -1):
                tmp = num & 1 << j
                if node.one and node.zero:
                    if tmp:
                        node = node.zero
                    else:
                        node = node.one
                    tmp_val += 1 << j
                else:
                    if (node.zero and tmp) or (node.one and not tmp):
                        tmp_val += 1 << j
                    node = node.one or node.zero
            ans = max(ans, tmp_val)
                                                
        return ans
    
    
# Bitmask Soultion: 

'''
Let us try to build the biggest XOR number binary digit by digit. So, the first question we are going to ask, 
is there two numbers, such that its XOR starts with 1...... (length is 32 bits). 
Howe we can find it? Let us use the idea of Problem 1: TwoSum: 
put all prefixes of lengh one to set and then try to find two numbers in this set such that their XOR starts 
with 1 (at first we have at most 2 elements in our set). Imagine that there are two numbers, which XOR starts with 1......, 
then the next question is there are two numbers with XOR starts with 11....., we again iterate through all numbers and 
find two of them with XOR starts with 11. It can happen that on the next step we did not find XOR starts with 111....., 
then we do not change our ans and on next step we are looking for XOR starts with 1101... and so on. So:

We iterate, starting from the first digit in binary representation of number and go to the right.
For each traversed digit we update our binary mask: in the beginning it is 10000...000, then it is 11000...000, 
11100...000 and in the end 11111...111. We need this mask to quickly extract information about first several digits 
of our number.
Create set of all possible starts of numbers, using num & mask: on the first iterations it will be first digit, on 
the next one first two digits and so on.
Apply TwoSum problem: if we found two numbers with XOR starting with start, then we are happy: we update our ans and 
break for inner loop: so we continue to look at the next digit.
Complexity: Time complexity is O(32n), because we traverse our numbers exactly 32 times. I do not like when this is 
called O(n) complexity, because we have quite big constant here. Space complexity is O(n).
'''
class Solution:
    def findMaximumXOR(self, nums):
        ans, mask = 0, 0
        for i in range(31, -1, -1):
            mask |= 1<<i
            found = set([num & mask for num in nums])
                
            start = ans | 1<<i
            for pref in found:
                if start^pref in found:
                    ans = start
                    break
        
        return ans


# THIS SOLUTION WORKS AND INTUITIVE TRIES WITH 0s and 1s
# I know there are more efficient soltions but happy that this works !

class Node:
    def __init__(self):
        self.left = None # 0
        self.right = None # 1

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = Node()
        
        # make trie
        for num in nums:
            cur = root
            for bit in range(30, -1, -1):
                # if the bit of the num is 1
                if num & (1 << bit):
                    if not cur.right:
                        cur.right = Node()
                    cur = cur.right 
                    
                # if the bit of the num is 0
                else:
                    if not cur.left:
                        cur.left = Node()
                    cur = cur.left
        
        # traverse trie 
        # if the bit of the num is 1 -> can traverse to 0 (left)
        # if the bit of the num is 0 -> can traverse to 1 (right)
        best = 0
        for num in nums:
            cur = root
            xor = 0
            for bit in range(30, -1, -1):
                # if the bit of the num is 1
                if num & (1 << bit):
                    if cur.left:
                        xor = (xor << 1) | 1
                        cur = cur.left
                    else:
                        xor = (xor << 1)
                        cur = cur.right
                # if the bit of the num is 0
                else:
                    if cur.right:
                        xor = (xor << 1) | 1
                        cur = cur.right
                    else:
                        xor = (xor << 1)
                        cur = cur.left
            best = max(best, xor)
        return best
