'''
3287. Find the Maximum Sequence Value of Array
Hard
Companies
Hint
You are given an integer array nums and a positive integer k.

The value of a sequence seq of size 2 * x is defined as:

(seq[0] OR seq[1] OR ... OR seq[x - 1]) XOR (seq[x] OR seq[x + 1] OR ... OR seq[2 * x - 1]).
Return the maximum value of any 
subsequence
 of nums having size 2 * k.

 

Example 1:

Input: nums = [2,6,7], k = 1

Output: 5

Explanation:

The subsequence [2, 7] has the maximum value of 2 XOR 7 = 5.

Example 2:

Input: nums = [4,2,5,6,7], k = 2

Output: 2

Explanation:

The subsequence [4, 5, 6, 7] has the maximum value of (4 OR 5) XOR (6 OR 7) = 2.

 

Constraints:

2 <= nums.length <= 400
1 <= nums[i] < 27
1 <= k <= nums.length / 2
'''

class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        # make a look up dp from right to left and left to right
        # then check both at the same time at the end
        # 
        # right_to_left = {
        #     i : {
        #         used : {
        #             2, 6, 7 | 0
        #         }
        #     }
        # }

        # LEFT TO RIGHT
        N = len(nums)
        lefts = {-1: {0: set([0])}}
        for i in range(N):
            lefts[i] = {}
            # first, copy over the memoized values from i-1
            for used, bitmasks in lefts[i-1].items():
                # copy
                lefts[i][used] = set(bitmasks)

            for used, bitmasks in lefts[i-1].items():
                # skip any key values greater than k, we will never use them
                if used+1 > k:
                    continue
                if used+1 not in lefts[i]:
                    lefts[i][used+1] = set([])
                for bitmask in bitmasks:
                    lefts[i][used+1].add(bitmask|nums[i])
        # print(lefts)
    
        # RIGHT TO LEFT
        rights = {N: {0: set([0])}}
        for i in range(N-1, -1, -1):
            rights[i] = {}
            # first, copy over the memoized values from i-1
            for used, bitmasks in rights[i+1].items():
                # copy
                rights[i][used] = set(bitmasks)

            for used, bitmasks in rights[i+1].items():
                # skip any key values greater than k, we will never use them
                if used+1 > k:
                    continue
                if used+1 not in rights[i]:
                    rights[i][used+1] = set([])
                for bitmask in bitmasks:
                    rights[i][used+1].add(bitmask|nums[i])
        # print(rights)

        # LOOK UP AND CHECK
        best = 0
        for i in range(k, N-k+1):
            for l in lefts[i-1][k]:
                for r in rights[i][k]:
                    best = max(best, l^r)
        return best