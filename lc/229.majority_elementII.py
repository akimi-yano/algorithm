# 229. Majority Element II
# Medium

# 1985

# 185

# Add to List

# Share
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Note: The algorithm should run in linear time and in O(1) space.

# Example 1:

# Input: [3,2,3]
# Output: [3]
# Example 2:

# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        '''
        step0: understand how many candiates are possible at most: N/3 -> at most 2 candidate
        
        step1: find candidate
            a) initialize an empty dictionary 
            b) iterate  through the input array
            c) if the elem is in dictionary, increment by 1  
            d) if its not in the dictionary but the length of the dictionary is less than 2, add it to the  dictionary with initial value of 1
            e) if its not in the dictionary and the length of the dictionary is 2 or more, for all the existing elements in the dictionary, decrement by 1 -> if its less than 0 -> delete from the dictionary
        
        step2: verify the count to see if its more than threshhold
            a) reset the count of all the elements in the dictionary to 0 and iterate through the input arr to count the frequency
            b) initialize an answer array
            c) iterate through the dictionary and if the count is larger than len(nums)/3 -> append the elem to the ans arr
            d) return the ans arr

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
    
