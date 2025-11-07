'''
2528. Maximize the Minimum Powered City
Hard
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed integer array stations of length n, where stations[i] represents the number of power stations in the ith city.

Each power station can provide power to every city in a fixed range. In other words, if the range is denoted by r, then a power station at city i can provide power to all cities j such that |i - j| <= r and 0 <= i, j <= n - 1.

Note that |x| denotes absolute value. For example, |7 - 5| = 2 and |3 - 10| = 7.
The power of a city is the total number of power stations it is being provided power from.

The government has sanctioned building k more power stations, each of which can be built in any city, and have the same range as the pre-existing ones.

Given the two integers r and k, return the maximum possible minimum power of a city, if the additional power stations are built optimally.

Note that you can build the k power stations in multiple cities.

 

Example 1:

Input: stations = [1,2,4,5,0], r = 1, k = 2
Output: 5
Explanation: 
One of the optimal ways is to install both the power stations at city 1. 
So stations will become [1,4,4,5,0].
- City 0 is provided by 1 + 4 = 5 power stations.
- City 1 is provided by 1 + 4 + 4 = 9 power stations.
- City 2 is provided by 4 + 4 + 5 = 13 power stations.
- City 3 is provided by 5 + 4 = 9 power stations.
- City 4 is provided by 5 + 0 = 5 power stations.
So the minimum power of a city is 5.
Since it is not possible to obtain a larger power, we return 5.
Example 2:

Input: stations = [4,4,4,4], r = 0, k = 3
Output: 4
Explanation: 
It can be proved that we cannot make the minimum power of a city greater than 4.
 

Constraints:

n == stations.length
1 <= n <= 105
0 <= stations[i] <= 105
0 <= r <= n - 1
0 <= k <= 109

'''

class Solution:
    def maxPower(self, stations, r, k):
        n = len(stations)
        df = [0] * (n + 5)
        
        # Build initial power difference array
        for i, j in enumerate(stations):
            df[max(0, i - r)] += j
            df[min(n - 1, i + r) + 1] -= j
        
        # Minimum current power; large upper bound for binary search
        lo, hi = min(accumulate(df[:n])), 2 * 10**10

        def check(mid):
            diff = df[:]
            cur, cnt = 0, 0
            for i in range(n):
                cur += diff[i]
                if cur < mid:
                    need = mid - cur
                    cnt += need
                    if cnt > k:
                        return False
                    cur = mid
                    # Reduce effect after range ends
                    diff[min(n - 1, i + 2 * r) + 1] -= need
            return True

        # Binary search for max feasible min power
        while lo < hi:
            mid = (lo + hi + 1) >> 1
            if check(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo