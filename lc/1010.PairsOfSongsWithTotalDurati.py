# 1010. Pairs of Songs With Total Durations Divisible by 60
# Medium

# 923

# 68

# Add to List

# Share
# You are given a list of songs where the ith song has a duration of time[i] seconds.

# Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

 

# Example 1:

# Input: time = [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60
# Example 2:

# Input: time = [60,60,60]
# Output: 3
# Explanation: All three pairs have a total duration of 120, which is divisible by 60.
 

# Constraints:

# 1 <= time.length <= 6 * 104
# 1 <= time[i] <= 500


# This approach does not work - TLE

# class Solution:
#     def numPairsDivisibleBy60(self, time: List[int]) -> int:
#         count = 0
#         for i in range(len(time)):
#             for j in range(i+1, len(time)):
#                 if (time[i]+time[j]) % 60 == 0:
#                     count += 1
#         return count


# This solution works !
'''
if 45, the other half should be 15

45: 5
15: 3 

then ans += 5 * 3 since they are interested in all the combinations

use counter dictionary and math.comb()
'''

from collections import Counter
import math
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counts = Counter([elem%60 for elem in time])
        ans = 0
        key_val = list(counts.items())
        for k, v in key_val:
            if (k == 0 or k==60//2):
                if v>=2:
                    ans += math.comb(v,2)
                    del counts[k]
            elif 60-k in counts:
                ans += counts[60-k] * v
                del counts[k]
                del counts[60-k]
        return ans 