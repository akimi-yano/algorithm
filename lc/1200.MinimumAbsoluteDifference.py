# 1200. Minimum Absolute Difference
# Easy

# 558

# 30

# Add to List

# Share
# Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements. 

# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

# a, b are from arr
# a < b
# b - a equals to the minimum absolute difference of any two elements in arr
 

# Example 1:

# Input: arr = [4,2,1,3]
# Output: [[1,2],[2,3],[3,4]]
# Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
# Example 2:

# Input: arr = [1,3,6,10,15]
# Output: [[1,3]]
# Example 3:

# Input: arr = [3,8,-10,23,19,-4,-14,27]
# Output: [[-14,-10],[19,23],[23,27]]
 

# Constraints:

# 2 <= arr.length <= 10^5
# -10^6 <= arr[i] <= 10^6


# This solution works:

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        '''
        0 sort - nlogn
        1 find min abs diff - n
        2 generate array with this min abs diff - two sum - n
            create set
            iterate through the sorted arr
            remove 1 smaller one from dict
        '''
        arr.sort()
        
        min_abs_diff = float('inf')
        for i in range(1, len(arr)):
            min_abs_diff = min(min_abs_diff, abs(arr[i-1] - arr[i]))
        
        all_nums = set([])
        for num in arr:
            all_nums.add(num)

        ans = []
        for num in arr:
            the_other = min_abs_diff + num
            if the_other in all_nums:
                ans.append([num, the_other])
            all_nums.remove(num)
        return ans
            



# This solution works - optimization:

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        prev = float('-inf')
        best = float('inf')
        pairs = []
        for num in arr:
            if num - prev < best:
                best = num - prev
                pairs = [(prev, num)]
            elif num - prev == best:
                pairs.append((prev, num))
            prev = num
        return pairs