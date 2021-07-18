# 927. Three Equal Parts
# Hard

# 567

# 93

# Add to List

# Share
# You are given an array arr which consists of only zeros and ones, divide the array into three non-empty parts such that all of these parts represent the same binary value.

# If it is possible, return any [i, j] with i + 1 < j, such that:

# arr[0], arr[1], ..., arr[i] is the first part,
# arr[i + 1], arr[i + 2], ..., arr[j - 1] is the second part, and
# arr[j], arr[j + 1], ..., arr[arr.length - 1] is the third part.
# All three parts have equal binary values.
# If it is not possible, return [-1, -1].

# Note that the entire part is used when considering what binary value it represents. For example, [1,1,0] represents 6 in decimal, not 3. Also, leading zeros are allowed, so [0,1,1] and [1,1] represent the same value.

 

# Example 1:

# Input: arr = [1,0,1,0,1]
# Output: [0,3]
# Example 2:

# Input: arr = [1,1,0,1,1]
# Output: [-1,-1]
# Example 3:

# Input: arr = [1,1,0,0,1]
# Output: [0,2]
 

# Constraints:

# 3 <= arr.length <= 3 * 104
# arr[i] is 0 or 1


# This solution works:

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        # if all zeros
        if not sum(arr):
            return [0, 2]
        
        ans = [-1, -1]
        
        # if number of ones is not divisible by 3
        if sum(arr) % 3:
            return ans
        
        # calculate number of ones in each section
        ones = sum(arr) // 3
        
        trailing_zeros = 0
        for bit in reversed(arr):
            if bit:
                break
            trailing_zeros += 1
        
        first = 0
        cur_ones = 0
        i = 0
        while i < len(arr):
            first <<= 1
            first |= arr[i]
            if arr[i]:
                cur_ones += 1
            i += 1
            if cur_ones == ones:
                for _ in range(trailing_zeros):
                    # if there aren't enough trailing zeros
                    if i >= len(arr) or arr[i]:
                        return [-1, -1]
                    first <<= 1
                    i += 1
                break
        first_idx = i - 1
        
        second = 0
        cur_ones = 0
        while i < len(arr):
            second <<= 1
            second |= arr[i]
            if arr[i]:
                cur_ones += 1
            i += 1
            if cur_ones == ones:
                for _ in range(trailing_zeros):
                    # if there aren't enough trailing zeros
                    if i >= len(arr) or arr[i]:
                        return [-1, -1]
                    second <<= 1
                    i += 1
                break
        if first != second:
            return [-1, -1]
        third_idx = i
        
        third = 0
        cur_ones = 0
        while i < len(arr):
            third <<= 1
            third |= arr[i]
            if arr[i]:
                cur_ones += 1
            i += 1
            if cur_ones == ones:
                for _ in range(trailing_zeros):
                    # if there aren't enough trailing zeros
                    if i >= len(arr) or arr[i]:
                        return [-1, -1]
                    third <<= 1
                    i += 1
                break
        if first != third:
            return [-1, -1]
        return [first_idx, third_idx]
