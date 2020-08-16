# 229. Majority Element II

# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Note: The algorithm should run in linear time and in O(1) space.

# Example 1:

# Input: [3,2,3]
# Output: [3]
# Example 2:

# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]


# IMPORTANT:
'''
more than 1/3 ... there  are at most 2 of these numbers

-----------N-----------
--1/3-- --1/3-- --1/3--

since its more than 1/3 there are at most 2

# Boyer-Moore Majority Vote algorithm

'''

# Python O(1) aux space sol. by BM vote algorithm.

# Hint:

#1.
# Think of Leetcode #169 Majority Element and Boyer–Moore majority vote algorithm

#2.
# There are at most two majority elements in array, with threshold = floor( n / 3 )

# This can be proved by contradiction method:
# Assume k majority elements, where k ≧ 3,
# then array size n > k * ( n / 3) ≧ 3 * ( n / 3) = n. ( conflict by n > n )

# Algorithm:

# Implement Boyer–Moore majority vote algorithm with threshold = floor( n / 3 )

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        # a list of majority elements
        majority = []
        
        # threshold for majority validation and verification
        threshold = len(nums) // 3
        
        # Record for possible majority candidates, at most two majority elements is allowed by math-proof.
        # - this is constant  cuz it does not grow the size as N increases
        candidate = [0, 0]
        
        # Voting for majority candidates - this is constant  cuz it does not grow the size as N increases
        voting = [0, 0]
        
        ## Step_#1:
        # Find possible majority candidates
        for number in nums:
            
            if number == candidate[0]:
                # up vote to first candidate
                voting[0] += 1
                
            elif number == candidate[1]:
                # up vote to second candidate
                voting[1] += 1
            
            elif not voting[0]:
                # set first candidate
                candidate[0] = number
                voting[0] = 1
                
            elif not voting[1]:
                # set second candidate
                candidate[1] = number
                voting[1] = 1
                
            else:
                # down vote for both if mis-match
                voting[0] -= 1
                voting[1] -= 1
        
        
        ## Step_#2:
        # Validation:
        voting = [0, 0]
        
        for number in nums:
            
            if number == candidate[0]:
                # update up vote for first candidate
                voting[0] += 1
                
            elif number == candidate[1]:
                # update up vote for second candidate
                voting[1] += 1
        
        
        for i, vote in enumerate(voting):
            
            # Verify majority by threshold
            if vote > threshold:
                majority.append( candidate[i] )
            
            
        return majority
        
# Related leetcode challenge:

# Leetcode #169 Majority Element

# Reference:
# [1] Boyer–Moore majority vote algorithm








# Did this with dictionary :) slight optimization !!! and intuitive !!!! Happy with my answer that works !

# Time: O(N)
# Space: O(1)

# Eye opening Boyer-Moore Majority Vote algorithm !!!!!

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        '''
        step0: understand how many candiates are possible at most: N/3 -> at most 2 candidate
        step1: find candidate
        step2: verify the count to see if its more than threshhold

        '''
        # step 1: find candidate
        candidates = {}
        for num in nums:
            if num in candidates:
                candidates[num]  += 1
            # step 0: keep the storage constant # 
            elif len(candidates)  < 2:
                candidates[num] = 1
            else:
                keys = list(candidates.keys())
                for key in keys:
                    candidates[key] -= 1
                    if candidates[key] < 1:
                        del candidates[key]
        # step 2: verify
        for candidate in candidates:
            candidates[candidate] = 0
        for num in nums:
            if num in candidates:
                candidates[num] += 1
        ans = []
        for candidate, count in candidates.items():
            if count > len(nums) / 3:
                ans.append(candidate)
        return ans