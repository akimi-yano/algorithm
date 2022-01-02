# 1010. Pairs of Songs With Total Durations Divisible by 60
# Medium

# 2043

# 94

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


# This solution works:


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # modding after summing and summing after modding are the same !
        counts = {}
        for t in time:
            modded_num = t%60
            if modded_num not in counts:
                counts[modded_num] = 0
            counts[modded_num] += 1
        
        ans = 0
        # 0 and 30 - use combination
        for num in range(31):
            if num in counts:
                the_other = 60-num
                if the_other == num:
                    ans += math.comb(counts[num], 2)
                elif num == 0:
                    ans += math.comb(counts[num], 2)
                else:
                    if the_other in counts:
                        ans += counts[the_other] * counts[num]
        return ans
                    