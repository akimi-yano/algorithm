# 164. Maximum Gap
# Hard

# 1397

# 236

# Add to List

# Share
# Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

# You must write an algorithm that runs in linear time and uses linear extra space.

 

# Example 1:

# Input: nums = [3,6,9,1]
# Output: 3
# Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
# Example 2:

# Input: nums = [10]
# Output: 0
# Explanation: The array contains less than 2 elements, therefore return 0.
 

# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 109

# This solution works:

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        '''
        This is quite difficult problem if you never used the idea of bucket sort. Let us divide all range of numbers into n-1 cells. We will talk a bit later, why it is n-1 and not other number. It is simpler to look at example:

        nums = [3,14,15,83,6,4,19,20,40]. Then we have 8 buckets, with numbers 0,1,2,3,4,5,6,7, some of them are empty:

                0: [3, 6, 4]
                1: [14, 15, 19, 20]
                3: [40]
                7: [83]

        How we choose what to put where: we have range [3-----83], which we separated into n-1 groups: [3--13), [13--23), ..., [73--83]. Note, that numbers are not sorted inside groups. Now, let us notice one simple thing: there can not be maximum gap between sorted values of array inside each bucket. Why? Because there is n-1 gaps with total difference hi - lo, so by pigeonhole principle, there is difference which is bigger or equal than (hi - lo)/(n-1): indeed if all differences are smaller than this value, than total sum will be smaller than (hi - lo). So, it suffies to look only at the differences between adjacent buckets and moreover it is difference between smallest number of one buckets and biggest value of previous bucket.

        So, here are to following steps of our algorithm:

        Distribute numbers to buckets. Be careful with the biggest one, I put it to n-2-th bucket, but if you put it to n-1 th, it will also be OK.
        Find minimum and maximum in each buckets, we do not need anything else.
        Iterate through buckets and check every difference between smallest element in one bucket and biggest in previous. Note, that here we also will check differences between say 1-st and 3-rd buckets if we have empty 2-nd bucket.

        Complexity: Time complexity is O(n): we traversed our data several times, space complexity is O(n) to keep buckets.
        '''
        lo, hi, n = min(nums), max(nums), len(nums)
        if n <= 2 or hi == lo: return hi - lo
        B = defaultdict(list)
        for num in nums:
            ind = n-2 if num == hi else (num - lo)*(n-1)//(hi-lo)
            B[ind].append(num)
            
        cands = [[min(B[i]), max(B[i])] for i in range(n-1) if B[i]]
        return max(y[0]-x[1] for x, y in zip(cands, cands[1:]))