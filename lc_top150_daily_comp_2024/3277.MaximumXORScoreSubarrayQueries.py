'''
3277. Maximum XOR Score Subarray Queries
Solved
Hard
Topics
Companies
Hint
You are given an array nums of n integers, and a 2D integer array queries of size q, where queries[i] = [li, ri].

For each query, you must find the maximum XOR score of any 
subarray
 of nums[li..ri].

The XOR score of an array a is found by repeatedly applying the following operations on a so that only one element remains, that is the score:

Simultaneously replace a[i] with a[i] XOR a[i + 1] for all indices i except the last one.
Remove the last element of a.
Return an array answer of size q where answer[i] is the answer to query i.

 

Example 1:

Input: nums = [2,8,4,32,16,1], queries = [[0,2],[1,4],[0,5]]

Output: [12,60,60]

Explanation:

In the first query, nums[0..2] has 6 subarrays [2], [8], [4], [2, 8], [8, 4], and [2, 8, 4] each with a respective XOR score of 2, 8, 4, 10, 12, and 6. The answer for the query is 12, the largest of all XOR scores.

In the second query, the subarray of nums[1..4] with the largest XOR score is nums[1..4] with a score of 60.

In the third query, the subarray of nums[0..5] with the largest XOR score is nums[1..4] with a score of 60.

Example 2:

Input: nums = [0,7,3,2,8,5,1], queries = [[0,3],[1,5],[2,4],[2,6],[5,6]]

Output: [7,14,11,14,5]

Explanation:

Index	nums[li..ri]	Maximum XOR Score Subarray	Maximum Subarray XOR Score
0	[0, 7, 3, 2]	[7]	7
1	[7, 3, 2, 8, 5]	[7, 3, 2, 8]	14
2	[3, 2, 8]	[3, 2, 8]	11
3	[3, 2, 8, 5, 1]	[2, 8, 5, 1]	14
4	[5, 1]	[5]	5
 

Constraints:

1 <= n == nums.length <= 2000
0 <= nums[i] <= 231 - 1
1 <= q == queries.length <= 105
queries[i].length == 2 
queries[i] = [li, ri]
0 <= li <= ri <= n - 1
'''
# This approach works ! This way is the easiest to understand for me.

class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:       
        '''
        N = 4 [a,b,c,d]

        l       r
        a   b   c   d
          ab  bc  cd
            ac   bd
              acbd

        
        '''
        # 1) make chart like pascals triangles
        pascals = [nums]
        while len(pascals[-1]) != 1:
            temp = []
            for i in range(len(pascals[-1])-1):
                temp.append(pascals[-1][i] ^ pascals[-1][i+1])
            pascals.append(temp)
        # print(pascals)

        # 2) traverse the graph to update the best one
        # change each value of the triangle to be the maximum of all its ancestors 
        for row in range(1, len(pascals)):
            for col in range(len(pascals[row])):
                pascals[row][col] = max(pascals[row-1][col], pascals[row-1][col+1], pascals[row][col])
        # print(pascals)
        ans = []
        for l, r in queries:
            ans.append(pascals[r-l][l])
        return ans
    

# Time: O(N^2 + Q)
# Space: O(N^2 + Q)