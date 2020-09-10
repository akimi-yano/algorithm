# 532. K-diff Pairs in an Array
# Easy

# 678

# 1395

# Add to List

# Share
# Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

# Example 1:
# Input: [3, 1, 4, 1, 5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# Although we have two 1s in the input, we should only return the number of unique pairs.
# Example 2:
# Input:[1, 2, 3, 4, 5], k = 1
# Output: 4
# Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
# Example 3:
# Input: [1, 3, 1, 5, 4], k = 0
# Output: 1
# Explanation: There is one 0-diff pair in the array, (1, 1).
# Note:
# The pairs (i, j) and (j, i) count as the same pair.
# The length of the array won't exceed 10,000.
# All the integers in the given input belong to the range: [-1e7, 1e7].




# THIS SOLUTION WORKS !:

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        '''
        key : [index]
        
        (smaller,larger) -> put it into set 
        
        return len(the set)
        '''
        memo = {}
        for i,num in enumerate(nums):
            if num not in memo:
                memo[num]=[]
            memo[num].append(i)

        ans = set([])
        for i, num in enumerate(nums):
            if num+k in memo:
                for idx in memo[num+k]:
                    if idx!=i:
                        if num>num+k:
                            ans.add((num+k,num))
                        else:
                            ans.add((num,num+k))
            if num-k in memo:
                for idx in memo[num-k]:
                    if idx!=i:
                        if num>num-k:
                            ans.add((num-k,num))
                        else:
                            ans.add((num,num-k))
        return len(ans)





# Other solutions:
'''
Count the elements with Counter
If k > 0, for each element i, check if i + k exist.
If k == 0, for each element i, check if count[i] > 1


Explanation
Time O(N)
Space O(N)


Python
'''
import collections

def findPairs(self, nums, k):
        res = 0
        c = collections.Counter(nums)
        for i in c:
            if k > 0 and i + k in c or k == 0 and c[i] > 1:
                res += 1
        return res
    
'''
which equals to:
'''

def findPairs(self, nums, k):
        c = collections.Counter(nums)
        return  sum(k > 0 and i + k in c or k == 0 and c[i] > 1 for i in c)
    
    
    
    
    # interesting solution :
    
    class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        if k == 0:
            return sum([1 for val in Counter(nums).values() if val > 1])
        arr = list(set(nums))
        arr.sort()
        i, j = 0, 1
        ans = 0
        while j < len(arr):
            if arr[j] - arr[i] < k:
                j += 1
            elif arr[j] - arr[i] > k:
                i += 1
            else:
                ans += 1
                i += 1
        return ans

# another solution :

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        if k == 0:
            return sum([1 for val in Counter(nums).values() if val > 1])
        s = set(nums)
        return sum([1 for num in s if num-k in s])