# 1734. Decode XORed Permutation
# Medium

# 151

# 5

# Add to List

# Share
# There is an integer array perm that is a permutation of the first n positive integers, where n is always odd.

# It was encoded into another integer array encoded of length n - 1, such that encoded[i] = perm[i] XOR perm[i + 1]. For example, if perm = [1,3,2], then encoded = [2,1].

# Given the encoded array, return the original array perm. It is guaranteed that the answer exists and is unique.

 

# Example 1:

# Input: encoded = [3,1]
# Output: [1,2,3]
# Explanation: If perm = [1,2,3], then encoded = [1 XOR 2,2 XOR 3] = [3,1]
# Example 2:

# Input: encoded = [6,5,4,6]
# Output: [2,4,1,5,3]
 

# Constraints:

# 3 <= n < 105
# n is odd.
# encoded.length == n - 1

# This solution works:

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        '''
                         this          this
        encoded:  a0^a1, a1^a2, a2^a3, a3^a4
        original: a0,  a1,    a2,    a3,    a4
        
        XOR these two:
        all_except0 = a1^a2 ^ a3^a4 (this ^ this - second one from the beginning and skip 1)
        all_nums_1toN = 1 ^ 2 ^ 3 ^ 4 ^ 5
        then we get:  a0
        once we get a0, we itearate through encoded arr to find all the sequence
        '''
        all_except0 = 0
        for i, num in enumerate(encoded):
            if i % 2:
                all_except0 ^= num
        
        N = len(encoded)+1
        all_nums_1toN = 0
        for num in range(1, N+1):
            all_nums_1toN ^= num
            
        prev = all_except0 ^ all_nums_1toN
        ans = []
        for num in encoded:
            ans.append(prev)
            prev = prev ^ num
        ans.append(prev)
        return ans
        