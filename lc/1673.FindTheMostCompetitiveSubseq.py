# 1673. Find the Most Competitive Subsequence
# Medium

# 88

# 8

# Add to List

# Share
# Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.

# An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.

# We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first position where a and b differ, subsequence a has a number less than the corresponding number in b. For example, [1,3,4] is more competitive than [1,3,5] because the first position they differ is at the final number, and 4 is less than 5.

 

# Example 1:

# Input: nums = [3,5,2,6], k = 2
# Output: [2,6]
# Explanation: Among the set of every possible subsequence: {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]}, [2,6] is the most competitive.
# Example 2:

# Input: nums = [2,4,3,3,5,4,9,6], k = 4
# Output: [2,3,3,4]
 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109
# 1 <= k <= nums.length




# This approach does not work: - TLE

#     class Solution:
#     def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
#         # find a smallest numbers with k length - but cannot change the order 
#         @lru_cache(None)
#         def helper(tup, i):
#             if len(tup) == self.k:
#                 return (tup,)
#             if i >= len(nums):
#                 return ()
#             temp = []
            
#             new_tup = tuple(list(tup) + [nums[i]])
#             temp.extend(elem for elem in list(helper(new_tup, i+1)))
#             temp.extend(elem for elem in list(helper(tup, i+1)))
#             return tuple(temp)
#         self.k = k
#         all_options = helper((), 0)
#         # print(all_options)
#         return list(sorted(all_options)[0])


# This solution works !

'''
its gready with mono increasing stack !
'''
class Solution:
    def mostCompetitive(self, A, k) -> List[int]:
        # Use a mono incrasing stack.

        # Keep a mono incrasing stack as result.
        # If current element a is smaller then the last element in the stack,
        # we can replace it to get a smaller sequence.

        # Before we do this,
        # we need to check if we still have enough elements after.
        # After we pop the last element from stack,
        # we have stack.size() - 1 in the stack,
        # there are A.size() - i can still be pushed.
        # if stack.size() - 1 + A.size() - i >= k, we can pop the stack.

        # Then, is the stack not full with k element,
        # we push A[i] into the stack.

        # Finally we return stack as the result directly.

        # Complexity
        # Time O(n)
        # Space O(k)
        
        stack = []
        for i, a in enumerate(A):
            # check if we will still have enough number of elem to create k elements after removing this element
            while stack and stack[-1] > a and len(stack) - 1 + len(A) - i >= k:
                stack.pop()
            if len(stack) < k:
                stack.append(a)
        return stack