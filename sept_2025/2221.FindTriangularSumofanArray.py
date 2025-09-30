'''
2221. Find Triangular Sum of an Array
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed integer array nums, where nums[i] is a digit between 0 and 9 (inclusive).

The triangular sum of nums is the value of the only element present in nums after the following process terminates:

Let nums comprise of n elements. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n - 1.
For each index i, where 0 <= i < n - 1, assign the value of newNums[i] as (nums[i] + nums[i+1]) % 10, where % denotes modulo operator.
Replace the array nums with newNums.
Repeat the entire process starting from step 1.
Return the triangular sum of nums.

 

Example 1:


Input: nums = [1,2,3,4,5]
Output: 8
Explanation:
The above diagram depicts the process from which we obtain the triangular sum of the array.
Example 2:

Input: nums = [5]
Output: 5
Explanation:
Since there is only one element in nums, the triangular sum is the value of that element itself.
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 9
'''

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            new_nums = []
            for i in range(len(nums)-1):
                new_nums.append((nums[i] + nums[i+1])%10)
            nums = new_nums
        
        return nums[0]
    
    
# Better approach using Pascal's triangle 

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        '''
        use Pascal's triangle coefficients: each element in the final result is determined 
        by binomial coefficients multiplied by the original array values.

        このコードで comb、つまり組み合わせの計算が使われているのは、パスカルの三角形の性質を利用して、最終的に残る1つの数字を効率よく計算するため。
        一言でいうと、配列の各要素が最終結果に何回足されるかを、組み合わせの計算 comb(N-1, i) を使って一発で求めている。
        '''
        N = len(nums)
        res = 0
        for i in range(N):
            # Coefficient calculation: Use comb(N-1, i) to get the coefficient for position i
            # N-1個の中からi個を選ぶ組み合わせの数を計算
            res = (res + comb(N-1, i) * nums[i]) % 10
        return res