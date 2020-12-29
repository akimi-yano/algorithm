# 754. Reach a Number
# Medium

# 639

# 501

# Add to List

# Share
# You are standing at position 0 on an infinite number line. There is a goal at position target.

# On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

# Return the minimum number of steps required to reach the destination.

# Example 1:
# Input: target = 3
# Output: 2
# Explanation:
# On the first move we step from 0 to 1.
# On the second step we step from 1 to 3.
# Example 2:
# Input: target = 2
# Output: 3
# Explanation:
# On the first move we step from 0 to 1.
# On the second move we step  from 1 to -1.
# On the third move we step from -1 to 2.
# Note:
# target will be a non-zero integer in the range [-10^9, 10^9].


# This solution works !
class Solution:
    def reachNumber(self, target):
        target = abs(target)
        
        cur = 0
        steps = 0
        # keep on adding (1+2+...+n) until we are at or past the target
        while cur < target:
            steps += 1
            cur += steps
        
        # keep on adding until the difference between cur and target is even
        while (cur - target) % 2:
            steps += 1
            cur += steps

        # when we are:
        # 1. at or above target
        # 2. diff between cur and target is even
        # there is a way to "flip" one of the past summed elements from +k to -k
        # such that the difference is 2*k. k is guaranteed to exist because
        # we have added everything between 1 to n (where n >= k).
        return steps