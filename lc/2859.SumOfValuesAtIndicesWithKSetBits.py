'''
2859. Sum of Values at Indices With K Set Bits
Easy
13
0
Companies
You are given a 0-indexed integer array nums and an integer k.

Return an integer that denotes the sum of elements in nums whose corresponding indices have exactly k set bits in their binary representation.

The set bits in an integer are the 1's present when it is written in binary.

For example, the binary representation of 21 is 10101, which has 3 set bits.
 

Example 1:

Input: nums = [5,10,1,5,2], k = 1
Output: 13
Explanation: The binary representation of the indices are: 
0 = 0002
1 = 0012
2 = 0102
3 = 0112
4 = 1002 
Indices 1, 2, and 4 have k = 1 set bits in their binary representation.
Hence, the answer is nums[1] + nums[2] + nums[4] = 13.
Example 2:

Input: nums = [4,3,2,1], k = 2
Output: 1
Explanation: The binary representation of the indices are:
0 = 002
1 = 012
2 = 102
3 = 112
Only index 3 has k = 2 set bits in its binary representation.
Hence, the answer is nums[3] = 1.
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 105
0 <= k <= 10

'''

class Solution: 
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        N = len(nums)
        memo = {}
        for num in range(N):
            i = num
            count = 0
            while num:
                count += num & 1
                num >>= 1
            if count not in memo:
                memo[count] = []
            memo[count].append(i)
        
        ans = 0
        if k in memo:
            for idx in memo[k]:
                ans += nums[idx]
        return ans




# Also can use num & (num-1) to count the one bits:
    def countBit(num):
        if num == 0:
            return 0
        res = 1
        while num & (num-1):
            res += 1
            num &= num-1
        return res

'''

num & (num-1)

It's figuring out if n is either 0 or an exact power of two.

     <----- binary ---->
 n      n    n-1   n&(n-1)
--   ----   ----   -------
 0   0000   0111    0000 *
 1   0001   0000    0000 *
 2   0010   0001    0000 *
 3   0011   0010    0010
 4   0100   0011    0000 *
 5   0101   0100    0100
 6   0110   0101    0100
 7   0111   0110    0110
 8   1000   0111    0000 *
 9   1001   1000    1000
10   1010   1001    1000
11   1011   1010    1010
12   1100   1011    1000
13   1101   1100    1100
14   1110   1101    1100
15   1111   1110    1110


'''