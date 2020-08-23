# 1562. Find Latest Group of Size M

# Given an array arr that represents a permutation of numbers from 1 to n. You have a binary string of size n that initially has all its bits set to zero.

# At each step i (assuming both the binary string and arr are 1-indexed) from 1 to n, the bit at position arr[i] is set to 1. You are given an integer m and you need to find the latest step at which there exists a group of ones of length m. A group of ones is a contiguous substring of 1s such that it cannot be extended in either direction.

# Return the latest step at which there exists a group of ones of length exactly m. If no such group exists, return -1.



# Example 1:

# Input: arr = [3,5,1,2,4], m = 1
# Output: 4
# Explanation:
# Step 1: "00100", groups: ["1"]
# Step 2: "00101", groups: ["1", "1"]
# Step 3: "10101", groups: ["1", "1", "1"]
# Step 4: "11101", groups: ["111", "1"]
# Step 5: "11111", groups: ["11111"]
# The latest step at which there exists a group of size 1 is step 4.
# Example 2:

# Input: arr = [3,1,5,4,2], m = 2
# Output: -1
# Explanation:
# Step 1: "00100", groups: ["1"]
# Step 2: "10100", groups: ["1", "1"]
# Step 3: "10101", groups: ["1", "1", "1"]
# Step 4: "10111", groups: ["1", "111"]
# Step 5: "11111", groups: ["11111"]
# No group of size 2 exists during any step.
# Example 3:

# Input: arr = [1], m = 1
# Output: 1
# Example 4:

# Input: arr = [2,1], m = 2
# Output: 2


# Constraints:

# n == arr.length
# 1 <= n <= 10^5
# 1 <= arr[i] <= n
# All integers in arr are distinct.
# 1 <= m <= arr.length






# This solution does not work:

# class Solution:
#     def findLatestStep(self, arr: List[int], m: int) -> int:
#         binary = ['1' for _ in range(len(arr))]
#         total_steps = len(arr)
#         step = 0
#         for i in range(len(arr)-1,-1,-1):
#             binary[arr[i]-1] = '0'
#             step+=1
#             temp = "".join(binary).split('0')
#             print(temp)
#             for elem in temp:
#                 if len(elem) == m:
#                     return total_steps -step
#         return -1



# This solution works !!!

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        lengths = [0 for _ in range(len(arr))]

        m_count = 0
        best = -1
        for i, flip in enumerate(arr):
            flip_idx = flip - 1
            left_ones = right_ones = 0
            if flip_idx > 0:
                left_ones = lengths[flip_idx-1]
            if flip_idx < len(lengths) - 1:
                right_ones = lengths[flip_idx+1]
        
            length_sum = left_ones + 1 + right_ones
            if length_sum == m:
                m_count += 1
            lengths[flip_idx-left_ones] = length_sum
            lengths[flip_idx+right_ones] = length_sum
            if left_ones == m:
                m_count -= 1
            if right_ones == m:
                m_count -= 1
            
            if m_count > 0:
                best = i + 1
        return best