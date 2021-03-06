# 384. Shuffle an Array
# Medium

# 93

# 120

# Add to List

# Share
# Given an integer array nums, design an algorithm to randomly shuffle the array.

# Implement the Solution class:

# Solution(int[] nums) Initializes the object with the integer array nums.
# int[] reset() Resets the array to its original configuration and returns it.
# int[] shuffle() Returns a random shuffling of the array.
 

# Example 1:

# Input
# ["Solution", "shuffle", "reset", "shuffle"]
# [[[1, 2, 3]], [], [], []]
# Output
# [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

# Explanation
# Solution solution = new Solution([1, 2, 3]);
# solution.shuffle();    // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must be equally likely to be returned. Example: return [3, 1, 2]
# solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
# solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]

 

# Constraints:

# 1 <= nums.length <= 200
# -106 <= nums[i] <= 106
# All the elements of nums are unique.
# At most 5 * 104 calls will be made to reset and shuffle.

# This solution works:

import random
class Solution:

    def __init__(self, nums: List[int]):
        self.initial = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.initial

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        idx = None
        seen = set([None])
        new_arr = [None for _ in range(len(self.initial))]
        for i in range(len(self.initial)):
            while idx in seen:
                idx = random.randint(0, len(self.initial)-1)
            new_arr[idx] = self.initial[i]
            seen.add(idx)
        return new_arr


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()


# This solution works:

from itertools import permutations
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.original

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        ans = list(self.original)
        start = 0
        N = len(ans)
        while start < N - 1:
            idx = random.randint(start, N - 1)
            ans[start], ans[idx] = ans[idx], ans[start]
            start += 1
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()