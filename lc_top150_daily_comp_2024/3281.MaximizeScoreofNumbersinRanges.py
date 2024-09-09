'''
3281. Maximize Score of Numbers in Ranges
Solved
Medium
Companies
Hint
You are given an array of integers start and an integer d, representing n intervals [start[i], start[i] + d].

You are asked to choose n integers where the ith integer must belong to the ith interval. The score of the chosen integers is defined as the minimum absolute difference between any two integers that have been chosen.

Return the maximum possible score of the chosen integers.

 

Example 1:

Input: start = [6,0,3], d = 2

Output: 4

Explanation:

The maximum possible score can be obtained by choosing integers: 8, 0, and 4. The score of these chosen integers is min(|8 - 0|, |8 - 4|, |0 - 4|) which equals 4.

Example 2:

Input: start = [2,6,13,13], d = 5

Output: 5

Explanation:

The maximum possible score can be obtained by choosing integers: 2, 7, 13, and 18. The score of these chosen integers is min(|2 - 7|, |2 - 13|, |2 - 18|, |7 - 13|, |7 - 18|, |13 - 18|) which equals 5.

 

Constraints:

2 <= start.length <= 105
0 <= start[i] <= 109
0 <= d <= 109
'''

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        '''
        sort and binary search the score and check if we can get this score
        [0-3, 3-6, 6-9]
         p       ^

        goal: 5


        [0-2,100-2,101-103] 
            i
            100+2 < 0+51
        prev = 0
        
        d=2

        '''
        def can_get_the_score(goal):
            # print("calling to check goal: ", goal) 
            prev = start[0]
            for i in range(1, len(start)):
                # print(prev)
                if  (start[i]+d) < (prev + goal):
                    return False
                # need at least start[i] for the next round
                prev = max(start[i],(prev + goal))
            return True

        start.sort()
        left = 0
        right = 10 ** 10 # set a number that is impossible
        while left < right:
            mid = (left+right+1) // 2
            if can_get_the_score(mid):
                left = mid
            else: 
                right = mid - 1
        return left