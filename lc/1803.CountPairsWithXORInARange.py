# 1803. Count Pairs With XOR in a Range
# Hard

# 57

# 6

# Add to List

# Share
# Given a (0-indexed) integer array nums and two integers low and high, return the number of nice pairs.

# A nice pair is a pair (i, j) where 0 <= i < j < nums.length and low <= (nums[i] XOR nums[j]) <= high.

 

# Example 1:

# Input: nums = [1,4,2,7], low = 2, high = 6
# Output: 6
# Explanation: All nice pairs (i, j) are as follows:
#     - (0, 1): nums[0] XOR nums[1] = 5 
#     - (0, 2): nums[0] XOR nums[2] = 3
#     - (0, 3): nums[0] XOR nums[3] = 6
#     - (1, 2): nums[1] XOR nums[2] = 6
#     - (1, 3): nums[1] XOR nums[3] = 3
#     - (2, 3): nums[2] XOR nums[3] = 5
# Example 2:

# Input: nums = [9,8,4,2,1], low = 5, high = 14
# Output: 8
# Explanation: All nice pairs (i, j) are as follows:
# ​​​​​    - (0, 2): nums[0] XOR nums[2] = 13
#     - (0, 3): nums[0] XOR nums[3] = 11
#     - (0, 4): nums[0] XOR nums[4] = 8
#     - (1, 2): nums[1] XOR nums[2] = 12
#     - (1, 3): nums[1] XOR nums[3] = 10
#     - (1, 4): nums[1] XOR nums[4] = 9
#     - (2, 3): nums[2] XOR nums[3] = 6
#     - (2, 4): nums[2] XOR nums[4] = 5
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# 1 <= nums[i] <= 2 * 104
# 1 <= low <= high <= 2 * 104


# This solution works:

# 2 * 10 **4  = 20000

class TrieNode:
    def __init__(self):
        self.count = 0
        self.left = None # 0
        self.right = None # 1

class Solution:
    max_shift = 1<<15
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        self.root = TrieNode()
        self.low = low
        self.high = high

        ans = 0
        for num in nums:
            ans += self.root.count - self.xor_smaller(num) - self.xor_larger(num)
            self.add_to_trie(num)
        return ans
    
    def xor_smaller(self, num):
        cur = self.root
        mask = Solution.max_shift
        count = 0
        while mask:
            if cur is None:
                return count
            # if low's bit is 1
            if mask & self.low:
                # if num's bit is 1
                if mask & num:
                    count += cur.right.count if cur.right else 0
                    cur = cur.left
                # if num's bit is 0
                else:
                    count += cur.left.count if cur.left else 0
                    cur = cur.right
            # if low's bit is 0
            else:
                # if num's bit is 1
                if mask & num:
                    cur = cur.right
                # if num's bit is 0
                else:
                    cur = cur.left
            mask >>= 1
        return count
    
    def xor_larger(self, num):
        cur = self.root
        mask = Solution.max_shift
        count = 0
        while mask:
            if cur is None:
                return count
            # if high's bit is 1
            if mask & self.high:
                # if num's bit is 1
                if mask & num:
                    cur = cur.left
                # if num's bit is 0
                else:
                    cur = cur.right
            # if high's bit is 0
            else:
                # if num's bit is 1
                if mask & num:
                    count += cur.left.count if cur.left else 0
                    cur = cur.right
                # if num's bit is 0
                else:
                    count += cur.right.count if cur.right else 0
                    cur = cur.left
            mask >>= 1
        return count
    
    def add_to_trie(self, num):
        # add the count to the root
        self.root.count += 1
        cur = self.root
        mask = Solution.max_shift
        while mask:
            if num & mask:
                if cur.right is None:
                    cur.right = TrieNode()
                cur = cur.right
                cur.count += 1
            else:
                if cur.left is None:
                    cur.left = TrieNode()
                cur = cur.left
                cur.count += 1
            mask >>= 1
        