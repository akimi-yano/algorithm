'''
670. Maximum Swap
Solved
Medium
Topics
Companies
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

 

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
 

Constraints:

0 <= num <= 108
'''

class Solution:
    def maximumSwap(self, num: int) -> int:
        original_num = num
        nums = []
        while num:
            num, mod = divmod(num, 10)
            nums.append(mod)

        def reverse_num(vals):
            left = 0
            right = len(vals)-1
            while left < right:
                vals[left], vals[right] = vals[right], vals[left]
                left += 1
                right -= 1
            return vals

        reversed_num = reverse_num(nums)
        # print(reversed_num)
        ans = []
        for i in range(len(reversed_num)):
            for j in range(i+1, len(reversed_num)):
                if reversed_num[i] < reversed_num[j]:
                    reversed_num[i], reversed_num[j] = reversed_num[j], reversed_num[i]
                    ans.append(list(reversed_num))
                    reversed_num[i], reversed_num[j] = reversed_num[j], reversed_num[i]
        if len(ans) == 0:
            return original_num
        best = max(ans)
        # print(best)
        N = len(best)
        i = 0
        to_return = 0
        while best:
            to_return += best.pop() * 10 ** i
            i += 1

        return to_return
        

class Solution:
    def maximumSwap(self, num: int) -> int:
        '''
        At each digit, if there is a larger digit that occurs later, 
        we want the swap it with the largest such digit that occurs the latest.
        '''
        A = [int(c) for c in str(num)]
        last = {x: i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for d in range(9, x, -1):
                if last.get(d, -inf) > i:
                    A[i], A[last[d]] = A[last[d]], A[i]
                    return int("".join(map(str, A)))
        return num


