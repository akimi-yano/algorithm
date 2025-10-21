'''
3346. Maximum Frequency of an Element After Performing Operations I
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums and two integers k and numOperations.

You must perform an operation numOperations times on nums, where in each operation you:

Select an index i that was not selected in any previous operations.
Add an integer in the range [-k, k] to nums[i].
Return the maximum possible frequency of any element in nums after performing the operations.

 

Example 1:

Input: nums = [1,4,5], k = 1, numOperations = 2

Output: 2

Explanation:

We can achieve a maximum frequency of two by:

Adding 0 to nums[1]. nums becomes [1, 4, 5].
Adding -1 to nums[2]. nums becomes [1, 4, 4].
Example 2:

Input: nums = [5,11,20,20], k = 5, numOperations = 1

Output: 2

Explanation:

We can achieve a maximum frequency of two by:

Adding 0 to nums[1].
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
0 <= k <= 105
0 <= numOperations <= nums.length
'''

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        '''
        frequency counting approach combined with prefix sums to efficiently compute how many elements can be transformed to each possible target value
        '''
        max_val = max(nums) + k + 1 # +1 to avoid going out of bound
        count = [0] * max_val
        # 出現回数（頻度）を数えます。
        for num in nums:
            count[num] += 1
        # 頻度を累積和に変換します。
        for i in range(1, max_val):
            count[i] += count[i-1]
        # count[i] は「nums の中で i 以下の数値の総数」

        ans = 0
        for i in range(max_val):
            # ターゲット i の計算
            left = max(0, i-k)
            right = min(max_val-1, i+k)
            total = count[right] - (count[left-1] if left else 0)
            freq = count[i] - (count[i-1] if i else 0)
            # total - freq: 範囲 [left,right] の中にあり、かつ i でない要素の数（＝ i に変更できる候補の数）
            # min(numOperations, total - freq): 「操作回数の上限 (numOperations)」と「変更候補の数」のうち、小さい方（＝実際に i に変更できる数）
            # freq + ...: 「元々 i だった数」＋「今回 i に変更した数」
            ans = max(ans, freq + min(numOperations, total - freq))
        return ans        