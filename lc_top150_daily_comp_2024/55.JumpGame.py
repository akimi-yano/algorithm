'''
55. Jump Game
Solved
Medium
Topics
Companies
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105

'''

# This solution works:

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
               <- <- <- <-
        nums = [2,3,1,1,4]
                        g
                        4
        '''
        # set the goal_idx to be the last elem in the list
        goal_idx = len(nums)-1
        # move backwards and check if it can reach the goal, if so move the goal to left
        # start from -2 position
        for i in range(len(nums)-2, -1, -1):
            if (i + nums[i]) >= goal_idx:
                goal_idx = i
        return goal_idx == 0
   
   
# Time: O(N)
# Space: O(1)