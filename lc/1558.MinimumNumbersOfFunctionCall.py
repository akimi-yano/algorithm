# 1558. Minimum Numbers of Function Calls to Make Target Array

# Your task is to form an integer array nums from an initial array of zeros arr that is the same size as nums.

# Return the minimum number of function calls to make nums from arr.

# The answer is guaranteed to fit in a 32-bit signed integer.



# Example 1:

# Input: nums = [1,5]
# Output: 5
# Explanation: Increment by 1 (second element): [0, 0] to get [0, 1] (1 operation).
# Double all the elements: [0, 1] -> [0, 2] -> [0, 4] (2 operations).
# Increment by 1 (both elements)  [0, 4] -> [1, 4] -> [1, 5] (2 operations).
# Total of operations: 1 + 2 + 2 = 5.
# Example 2:

# Input: nums = [2,2]
# Output: 3
# Explanation: Increment by 1 (both elements) [0, 0] -> [0, 1] -> [1, 1] (2 operations).
# Double all the elements: [1, 1] -> [2, 2] (1 operation).
# Total of operations: 2 + 1 = 3.
# Example 3:

# Input: nums = [4,2,5]
# Output: 6
# Explanation: (initial)[0,0,0] -> [1,0,0] -> [1,0,1] -> [2,0,2] -> [2,1,2] -> [4,2,4] -> [4,2,5](nums).
# Example 4:

# Input: nums = [3,2,2,4]
# Output: 7
# Example 5:

# Input: nums = [2,4,8,16]
# Output: 8


# Constraints:

# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9



# This solution does not work 

#         zeros=set([])
#         count = 0
#         for i in range(len(nums)):
#             if nums[i] !=0 and nums[i]%2!=0:
#                 nums[i]-=1
#                 count+=1
#                 if nums[i]==0:
#                     zeros.add(i)

#         doubled = False
#         div_count = 0
#         while len(zeros)<len(nums):
#             for i in range(len(nums)):
#                 if nums[i]!=1:
#                     nums[i]//=2
#                     doubled = True
#                     if nums[i]==0:
#                         zeros.add(i)
                                        
#                 else:
#                     doubled = False
#                     break
#             if doubled:
#                 div_count+=1
#                 doubled = False
#             else:
#                 break
#         count+=div_count
#         print(nums)
#         return count

# This solution does not work

# class Solution:
#     def minOperations(self, nums: List[int]) -> int:
#         nums.sort(reverse=True)
     
#         self.count = 0
#         def sub(nums):
#             for i in range(len(nums)):
#                 if nums[i]%2!=0:
#                     nums[i]-=1
#                     self.count+=1
#             return nums
        
#         def divide_all(nums):
#             for k in range(len(nums)):
#                 if nums[k] == 0 or nums[k]%2==0:
#                     nums[k]//=2
#                 else:
#                     return []
#             return nums
        
#         def zeros(nums):
#             c = 0
#             for n in nums:
#                 if n==0:
#                     c+=1
#             return c
        
#         nums = sub(nums)
#         while zeros(nums)<len(nums):
#             temp = divide_all(nums)
#             if len(temp) == len(nums):
#                 nums = temp
#                 self.count+=1
#             elif sub(nums) != nums:
#                 nums = sub(nums)

#         return self.count

# This solution works !!!
class Solution:
    def minOperations(self, nums: List[int]) -> int:

        self.count = 0
        def sub(nums):
            for i in range(len(nums)):
                if nums[i]%2!=0:
                    nums[i]-=1
                    self.count+=1
            return nums
        
        def divide_all(nums):
            for k in range(len(nums)):
                if nums[k] == 0 or nums[k]%2==0:
                    nums[k]//=2
                else:
                    return []
            return nums
        
        def zeros(nums):
            c = 0
            for n in nums:
                if n==0:
                    c+=1
            return c
        
        nums = sub(nums)
        while zeros(nums)<len(nums):
            temp = divide_all(list(nums)) # make a copy so that it does not affect the global nums
            if len(temp) == len(nums):
                nums = temp
                self.count+=1
            else:
                # if you  get here, there is always an odd number - call sub() just once
                temp = sub(list(nums))  # make a copy so that it does not affect the global nums
                nums = temp

        return self.count
    
    
# Yay optimized my code!!!! - final solution 
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        self.count = 0
        def sub(nums):
            for i in range(len(nums)):
                if nums[i]%2!=0:
                    nums[i]-=1
                    self.count+=1
        
        def divide_all(nums):
            for k in range(len(nums)):
                nums[k]//=2
        
        sub(nums)
        while sum(nums) > 0:
            divide_all(nums)
            self.count+=1
            sub(nums)

        return self.count