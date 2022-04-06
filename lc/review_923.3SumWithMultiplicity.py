# 923. 3Sum With Multiplicity
# Medium

# 906

# 145

# Add to List

# Share
# Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

# As the answer can be very large, return it modulo 109 + 7.

 

# Example 1:

# Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
# Output: 20
# Explanation: 
# Enumerating by the values (arr[i], arr[j], arr[k]):
# (1, 2, 5) occurs 8 times;
# (1, 3, 4) occurs 8 times;
# (2, 2, 4) occurs 2 times;
# (2, 3, 3) occurs 2 times.
# Example 2:

# Input: arr = [1,1,2,2,2,2], target = 5
# Output: 12
# Explanation: 
# arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
# We choose one 1 from [1,1] in 2 ways,
# and two 2s from [2,2,2,2] in 6 ways.
 

# Constraints:

# 3 <= arr.length <= 3000
# 0 <= arr[i] <= 100
# 0 <= target <= 300


# This solution works:


class Solution:
    MOD = 10 ** 9 + 7
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ans = 0
        counts = Counter(arr)
        for first in range(101):
            for second in range(first, 101):
                third = target - first - second
                if third < second:
                    continue
                if first == second == third:
                    ans += math.comb(counts[first], 3)
                elif first == second:
                    ans += math.comb(counts[first], 2) * counts[third]
                elif second == third:
                    ans += math.comb(counts[second], 2) * counts[first]
                elif third == first:
                    ans += math.comb(counts[third], 2) * counts[second]
                else:
                    ans += counts[first] * counts[second] * counts[third]
        
        return ans % Solution.MOD