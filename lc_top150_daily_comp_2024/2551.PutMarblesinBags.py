'''
2551. Put Marbles in Bags
Hard
Topics
Companies
Hint
You have k bags. You are given a 0-indexed integer array weights where weights[i] is the weight of the ith marble. You are also given the integer k.

Divide the marbles into the k bags according to the following rules:

No bag is empty.
If the ith marble and jth marble are in a bag, then all marbles with an index between the ith and jth indices should also be in that same bag.
If a bag consists of all the marbles with an index from i to j inclusively, then the cost of the bag is weights[i] + weights[j].
The score after distributing the marbles is the sum of the costs of all the k bags.

Return the difference between the maximum and minimum scores among marble distributions.

 

Example 1:

Input: weights = [1,3,5,1], k = 2
Output: 4
Explanation: 
The distribution [1],[3,5,1] results in the minimal score of (1+1) + (3+1) = 6. 
The distribution [1,3],[5,1], results in the maximal score of (1+3) + (5+1) = 10. 
Thus, we return their difference 10 - 6 = 4.
Example 2:

Input: weights = [1, 3], k = 2
Output: 0
Explanation: The only distribution possible is [1],[3]. 
Since both the maximal and minimal score are the same, we return 0.
 

Constraints:

1 <= k <= weights.length <= 105
1 <= weights[i] <= 109
'''

import heapq
from itertools import pairwise

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        nums = [a + b for a, b in pairwise(weights)]
        return sum(heapq.nlargest(k - 1, nums)) - sum(heapq.nsmallest(k - 1, nums))

        '''
        the problem turns out to be,
        calculate the max/min sum of k - 1 numbers in
        A[0] + A[1], A[1] + A[2],..., A[n-1] + A[n]

        PAIRWISE:
        my_list = [1, 2, 3, 4, 5]

        for x, y in pairwise(my_list):
            print(x, y)

        # Expected output:
        # 1 2
        # 2 3
        # 3 4
        # 4 5

        NLARGEST:
        numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        largest_3 = heapq.nlargest(3, numbers)
        print(largest_3)  # Output: [9, 6, 5]

        NSMALLEST:
        numbers = [5, 1, 9, 3, 7, 2, 8, 4, 6]
        smallest_three = heapq.nsmallest(3, numbers)
        print(smallest_three)  # Output: [1, 2, 3]
        '''