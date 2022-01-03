# 1200. Minimum Absolute Difference
# Easy

# 1038

# 47

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
        arr.sort()
        ans = {}
        for i in range(len(arr)-1):
            abs_diff = abs(arr[i] - arr[i+1])
            if abs_diff not in ans:
                ans[abs_diff] = []
            ans[abs_diff].append([arr[i], arr[i+1]])
        
        to_return = list(ans.items())
        to_return.sort(key = lambda elem : elem[0])
        return to_return[0][1]
        

