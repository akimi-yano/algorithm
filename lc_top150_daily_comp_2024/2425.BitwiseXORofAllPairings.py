'''
2425. Bitwise XOR of All Pairings
Medium
Topics
Companies
Hint
You are given two 0-indexed arrays, nums1 and nums2, consisting of non-negative integers. There exists another array, nums3, which contains the bitwise XOR of all pairings of integers between nums1 and nums2 (every integer in nums1 is paired with every integer in nums2 exactly once).

Return the bitwise XOR of all integers in nums3.

 

Example 1:

Input: nums1 = [2,1,3], nums2 = [10,2,5,0]
Output: 13
Explanation:
A possible nums3 array is [8,0,7,2,11,3,4,1,9,1,6,3].
The bitwise XOR of all these numbers is 13, so we return 13.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 0
Explanation:
All possible pairs of bitwise XORs are nums1[0] ^ nums2[0], nums1[0] ^ nums2[1], nums1[1] ^ nums2[0],
and nums1[1] ^ nums2[1].
Thus, one possible nums3 array is [2,5,1,6].
2 ^ 5 ^ 1 ^ 6 = 0, so we return 0.
 

Constraints:

1 <= nums1.length, nums2.length <= 105
0 <= nums1[i], nums2[j] <= 109
'''

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        N1 = len(nums1)
        N2 = len(nums2)
        counts = Counter()

        for num1 in nums1:
            counts[num1] += N2
        
        for num2 in nums2:
            counts[num2] += N1
        
        ans = 0
        for k, v in counts.items():
            if v % 2:
                ans ^= k
        return ans

# Another way:

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        N1 = len(nums1)
        N2 = len(nums2)
        n1 = 0
        n2 = 0
        for num1 in nums1:
            n1 ^= num1
        
        for num2 in nums2:
            n2 ^= num2
        
        return ((N2%2) * n1) ^ ((N1%2) * n2)
