'''
2860. Happy Students
Medium
23
78
Companies
You are given a 0-indexed integer array nums of length n where n is the total number of students in the class. The class teacher tries to select a group of students so that all the students remain happy.

The ith student will become happy if one of these two conditions is met:

The student is selected and the total number of selected students is strictly greater than nums[i].
The student is not selected and the total number of selected students is strictly less than nums[i].
Return the number of ways to select a group of students so that everyone remains happy.

 

Example 1:

Input: nums = [1,1]
Output: 2
Explanation: 
The two possible ways are:
The class teacher selects no student.
The class teacher selects both students to form the group. 
If the class teacher selects just one student to form a group then the both students will not be happy. Therefore, there are only two possible ways.
Example 2:

Input: nums = [6,0,3,3,6,7,2,7]
Output: 3
Explanation: 
The three possible ways are:
The class teacher selects the student with index = 1 to form the group.
The class teacher selects the students with index = 1, 2, 3, 6 to form the group.
The class teacher selects all the students to form the group.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] < nums.length
'''

# This solution passed but I feel like there are some better ways and also need more confidence on the logical thinking.

class Solution:
    def countWays(self, nums: List[int]) -> int:
        '''
         @        @           @
         1  2  3  4  5  6  7  8 
        [0, 2, 3, 3, 6, 6, 7, 7]
      in 1  3  4  4  7  7  8  8
     out -1 1  2  2  5  5  6  6
            @  @  @  @  @   
     N = 8
      
      1 2 
     [1,1]
      2 2
         '''
        nums.sort()
        N = len(nums)
        ways = 0
        if nums[0] != 0:
            ways += 1

        for i in range(N):
            isValid = True
            if nums[i]+1 <= i+1:
                for k in range(i+1, N):
                    if nums[k] <= i+1:
                        isValid = False
                        break
                if isValid:
                    ways += 1
        return ways   
    

# This way is better: I think adding -inf and inf helpes a lot here.

class Solution:
    def countWays(self, nums: List[int]) -> int:
        '''
         @        @           @
         1  2  3  4  5  6  7  8 

        [0, 2, 3, 3, 6, 6, 7, 7]
        [0 | 2 ................]
      i     1             n-1

      Selected |    NOT Selected

        so nums[i-1] < i < nums[i] then it is ok 
 
        Intuition
        Consider our result N. It has to satisfy:

        strictly smaller than the smallest of the unselected
        strictly greater than the greatest of the selected

        So sort the array and try to cut it at each position, so that whatever on its left is selected, and whatever on its right is not selected.
        
        Approach
        1. Sort the nums
        2. Add -inf and inf to avoid checks on two array boarders
        3. Loop the nums, at each step:
           - check if we can fit-in the n at this position.
           - That is, check if the number of elements we iterated so far happens to be strictly greater than the left & strictly smaller than the right.
        
        Complexity
        Time complexity:
        O(n)O(n)O(n)

        Space complexity:
        O(1)O(1)O(1)
         '''
        nums += [float('-inf'), float('+inf')]
        nums.sort()
        ways = 0
        for i in range(1, len(nums)):
            if nums[i-1] < (i-1) < nums[i]:
                ways += 1
                
        return ways