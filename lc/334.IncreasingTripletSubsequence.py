# 334. Increasing Triplet Subsequence
# Medium

# 1813

# 144

# Add to List

# Share
# Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

# Formally the function should:

# Return true if there exists i, j, k
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
# Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

# Example 1:

# Input: [1,2,3,4,5]
# Output: true
# Example 2:

# Input: [5,4,3,2,1]
# Output: false



# This approach does not work :

# class Solution:
#     def increasingTriplet(self, nums: List[int]) -> bool:
#         smallest = min(nums)
#         idx = nums.index(smallest)
#         count = 0
#         for i in range(idx, len(nums)):
#             if nums[i] > smallest:
#                 count +=1
#                 smallest = nums[i]
#         return count >= 3


# This solution works !:

'''
we keep building on stack until either it gets all 3 valid elements and return True or it gets a number that is smaller than the
smallest element of the stack. In the latter case, we start building on the stack2 and swap the stack 2 with stack as soon as 
it builds up 2 elemts in stack 2
'''

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        stack = []
        stack2 = [float('inf')]
        for num in nums:
            if len(stack) < 1:
                stack.append(num)
            if len(stack) == 1:
                if stack[0] < num:
                    stack.append(num)
                elif stack[0] > num:
                    stack = [num]
            # [a,b], num
            # 1) b < num, then a < b < num, so return True
            # 2) a < num < b, then change to [a, num]
            # 3) num < a < b... make two stacks?
            #     [a, b], [num]
            else:
                if num > stack[-1]:
                    return True
                elif stack[1] > num > stack[0]:
                    stack[1] = num
                else:
                    if num > stack2[0]:
                        stack2.append(num)
                        stack = stack2
                        stack2 = [float('inf')]
                    elif num < stack2[0]:
                        stack2 = [num]
        return False
    
    
# This solution works !! - simplification:

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        '''
        first - keeps track of the first sequence
        second - keeps track of the second sequence
        return true if we find third one
        '''
        first = second = float('inf')
        for num in nums:
            if num < first:
                first = num
            elif first < num < second:
                second = num
            elif second < num:
                    return True
        return False