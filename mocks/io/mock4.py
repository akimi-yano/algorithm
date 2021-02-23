'''

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


Example 1:
Input: nums = [3,2,3]
Output: 3


Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

'''
'''
input array of nums
output val


invalid [1,1,1,2,2,2]

1 iterate


 [3,3,2]
     cur
val = None-> 3
count = 0 -> 1 -> 2 ->1

[2,2,1,1,1,2,2]
             c
val = 2
count= 1 -> 2 -> 1 -> 0 -> 1 -> 0 -> 1
'''




'''
Majority: ⌊n / 3⌋


Example 1:
Input: nums = [3,2,3]
Output: [3]

3/3 = 1 -> more than 1 time

Example 2:
Input: nums = [1]
Output: [1]

1/3 = 1 -> 1 time

Example 3:
Input: nums = [1,2]
Output: [1,2]

2/3 = 1 -> 1 time

[O,O,O]
 _ _ _
n/3

steps:

[3,3,3,2,2,4,1] -> 3
            cur

1) threshold = n//3 = 7//3 = 2


2) {3:1} -> candidate is 3


3) reset the count and traverse again 
is more than threshold? check by traversing the dictionary's value

return [3]


'''

# This solution works - optimization:
class Solution:
    def majorityElement(self, nums):
        val = None
        count = 0
        for num in nums:
            if count == 0: # initial cond
                val = num
                count = 1
            elif val == num: # same value +1
                count +=1
            else: # different value -1
                count-=1
        return val

# This solution works:
class Solution:
    def majorityElement(self, nums):
        val = None
        count = 0
        for num in nums:
            if val is None or val == num:
                val = num
                count +=1
            else:
                if count > 0:
                    count-=1
                else:
                    val = num
                    count += 1
        return val
s = Solution()
print(s.majorityElement([3,2,3])) #3
print(s.majorityElement([2,2,1,1,1,2,2])) #2
print(s.majorityElement([3,3,2])) # 3
print(s.majorityElement([-1,-1,2,3,0,-1,-1])) #-1
        
        
        