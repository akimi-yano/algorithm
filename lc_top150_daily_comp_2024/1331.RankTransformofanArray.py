'''
1331. Rank Transform of an Array
Solved
Easy
Topics
Companies
Hint
Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.
 

Example 1:

Input: arr = [40,10,20,30]
Output: [4,1,2,3]
Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.
Example 2:

Input: arr = [100,100,100]
Output: [1,1,1]
Explanation: Same elements share the same rank.
Example 3:

Input: arr = [37,12,28,9,100,56,80,5,12]
Output: [5,3,4,2,8,6,7,1,3]
 

Constraints:

0 <= arr.length <= 105
-109 <= arr[i] <= 109
'''

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        num_i = {}
        for i, num in enumerate(arr):
            if num not in num_i:
                num_i[num] = []
            num_i[num].append(i)
        
        val_is = sorted(list(num_i.items()))
        rank = 1
        for _, i_s in val_is:
            for i in i_s:
                arr[i] = rank
            rank += 1
        return arr
        
        '''
        [40,10,20,30]

        {
        40:[0],
        10:[1],
        20:[2],
        30:[3]
        }
        '''
