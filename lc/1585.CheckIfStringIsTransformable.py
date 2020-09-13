# 1585. Check If String Is Transformable With Substring Sort Operations
# Hard

# 21

# 2

# Add to List

# Share
# Given two strings s and t, you want to transform string s into string t using the following operation any number of times:

# Choose a non-empty substring in s and sort it in-place so the characters are in ascending order.
# For example, applying the operation on the underlined substring in "14234" results in "12344".

# Return true if it is possible to transform string s into string t. Otherwise, return false.

# A substring is a contiguous sequence of characters within a string.

 

# Example 1:

# Input: s = "84532", t = "34852"
# Output: true
# Explanation: You can transform s into t using the following sort operations:
# "84532" (from index 2 to 3) -> "84352"
# "84352" (from index 0 to 2) -> "34852"
# Example 2:

# Input: s = "34521", t = "23415"
# Output: true
# Explanation: You can transform s into t using the following sort operations:
# "34521" -> "23451"
# "23451" -> "23415"
# Example 3:

# Input: s = "12345", t = "12435"
# Output: false
# Example 4:

# Input: s = "1", t = "2"
# Output: false
 

# Constraints:

# s.length == t.length
# 1 <= s.length <= 105
# s and t only contain digits from '0' to '9'.


# This solution works !!!

'''
we start checking from the target string and we want to make sure that the after finding the number at the original string,
all the numbers on the left are larger than the target number we have -> if not immediately return False

since the numbers are only 0-9, we can use index and array (and queue) to store the indexes of each number
'''

from collections import deque

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        num_idxs = [deque([]) for _ in range(10)]
        for i, num_str in enumerate(s):
            num = int(num_str)
            num_idxs[num].append(i)
        # print(num_idxs)
        
        for target_num_str in t:
            target_num = int(target_num_str)
            if len(num_idxs[target_num]) < 1:
                return False
            num_idx = num_idxs[target_num].popleft()
            
            # check numbers smaller than target_num if they appear earlier in the string
            for smaller_num in range(target_num):
                if len(num_idxs[smaller_num]) > 0 and num_idxs[smaller_num][0] < num_idx:
                    return False
        return True