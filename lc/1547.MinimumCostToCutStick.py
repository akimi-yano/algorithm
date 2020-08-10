# 1547. Minimum Cost to Cut a Stick
# Hard

# 90

# 4

# Add to List

# Share
# Given a wooden stick of length n units. The stick is labelled from 0 to n. For example, a stick of length 6 is labelled as follows:


# Given an integer array cuts where cuts[i] denotes a position you should perform a cut at.

# You should perform the cuts in order, you can change the order of the cuts as you wish.

# The cost of one cut is the length of the stick to be cut, the total cost is the sum of costs of all cuts. When you cut a stick, it will be split into two smaller sticks (i.e. the sum of their lengths is the length of the stick before the cut). Please refer to the first example for a better explanation.

# Return the minimum total cost of the cuts.

 

# Example 1:


# Input: n = 7, cuts = [1,3,4,5]
# Output: 16
# Explanation: Using cuts order = [1, 3, 4, 5] as in the input leads to the following scenario:

# The first cut is done to a rod of length 7 so the cost is 7. The second cut is done to a rod of length 6 (i.e. the second part of the first cut), the third is done to a rod of length 4 and the last cut is to a rod of length 3. The total cost is 7 + 6 + 4 + 3 = 20.
# Rearranging the cuts to be [3, 5, 1, 4] for example will lead to a scenario with total cost = 16 (as shown in the example photo 7 + 4 + 3 + 2 = 16).
# Example 2:

# Input: n = 9, cuts = [5,6,1,4,2]
# Output: 22
# Explanation: If you try the given cuts ordering the cost will be 25.
# There are much ordering with total cost <= 25, for example, the order [4, 6, 5, 2, 1] has total cost = 22 which is the minimum possible.
 

# Constraints:

# 2 <= n <= 10^6
# 1 <= cuts.length <= min(n - 1, 100)
# 1 <= cuts[i] <= n - 1
# All the integers in cuts array are distinct.

# this solution works!

class Solution:
    def min_cut(self, left_cut_index, right_cut_index, stick_start, stick_end):
        key = (left_cut_index, right_cut_index, stick_start, stick_end)
        if key in self.memo:
            return self.memo[key]

        best_cut = float('inf')
        if left_cut_index > right_cut_index:
            best_cut = 0
        else:
            for cut_index in range(left_cut_index, right_cut_index + 1):
                cut = self.cuts[cut_index]
                stick_length = stick_end - stick_start
                left_stick_cost = self.min_cut(left_cut_index, cut_index - 1, stick_start, cut)
                right_stick_cost = self.min_cut(cut_index + 1, right_cut_index, cut, stick_end)
                best_cut = min(best_cut, stick_length + left_stick_cost + right_stick_cost)
        
        self.memo[key] = best_cut
        return best_cut

    def minCost(self, n: int, cuts: List[int]) -> int:
        self.cuts = cuts
        self.cuts.sort()
        self.memo = {}
        return self.min_cut(0, len(self.cuts)-1, 0, n)