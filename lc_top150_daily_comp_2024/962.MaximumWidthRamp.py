'''
962. Maximum Width Ramp
Solved
Medium
Topics
Companies
A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

 

Example 1:

Input: nums = [6,0,8,2,1,5]
Output: 4
Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
Example 2:

Input: nums = [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.
 

Constraints:

2 <= nums.length <= 5 * 104
0 <= nums[i] <= 5 * 104

'''

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # print(f'testing {nums}')
        pres = [(nums[0], 0)]
        best = 0
        for i in range(1, len(nums)):
            elem = nums[i]
            l, r = 0, len(pres)-1
            while l < r:
                m = (l+r)//2
                if pres[m][0] <= elem:
                    r = m
                else:
                    l = m + 1
            left_elem, left_index = pres[l]
            if left_elem <= elem:
                if best < i-left_index:
                    # print(f'Updating best to {i}')
                    best = max(best, i-left_index)
            if elem < pres[-1][0]:
                pres.append((elem, i))
                # print(f'added {elem}: {pres}')
        return best