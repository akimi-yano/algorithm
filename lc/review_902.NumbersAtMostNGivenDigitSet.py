# 902. Numbers At Most N Given Digit Set
# Hard

# 689

# 73

# Add to List

# Share
# Given an array of digits which is sorted in non-decreasing order. You can write numbers using each digits[i] as many times as we want. For example, if digits = ['1','3','5'], we may write numbers such as '13', '551', and '1351315'.

# Return the number of positive integers that can be generated that are less than or equal to a given integer n.

 

# Example 1:

# Input: digits = ["1","3","5","7"], n = 100
# Output: 20
# Explanation: 
# The 20 numbers that can be written are:
# 1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
# Example 2:

# Input: digits = ["1","4","9"], n = 1000000000
# Output: 29523
# Explanation: 
# We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
# 81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
# 2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
# In total, this is 29523 integers that can be written using the digits array.
# Example 3:

# Input: digits = ["7"], n = 8
# Output: 1
 

# Constraints:

# 1 <= digits.length <= 9
# digits[i].length == 1
# digits[i] is a digit from '1' to '9'.
# All the values in digits are unique.
# digits is sorted in non-decreasing order.
# 1 <= n <= 109


# This solution works:


'''
Intuition

As in Approach #1, call a positive integer X valid if X <= N and X only consists of digits from D.

Now let B = D.length. There is a bijection between valid integers and so called "bijective-base-B" numbers. For example, if D = ['1', '3', '5', '7'], then we could write the numbers '1', '3', '5', '7', '11', '13', '15', '17', '31', ... as (bijective-base-B) numbers '1', '2', '3', '4', '11', '12', '13', '14', '21', ....

It is clear that both of these sequences are increasing, which means that the first sequence is a contiguous block of valid numbers, followed by invalid numbers.

Our approach is to find the largest valid integer, and convert it into bijective-base-B from which it is easy to find its rank (position in the sequence.) Because of the bijection, the rank of this element must be the number of valid integers.

Continuing our example, if N = 64, then the valid numbers are '1', '3', ..., '55', '57', which can be written as bijective-base-4 numbers '1', '2', ..., '33', '34'. Converting this last entry '34' to decimal, the answer is 16 (3 * 4 + 4).

Algorithm

Let's convert N into the largest possible valid integer X, convert X to bijective-base-B, then convert that result to a decimal answer. The last two conversions are relatively straightforward, so let's focus on the first part of the task.

Let's try to write X one digit at a time. Let's walk through an example where D = ['2', '4', '6', '8']. There are some cases:

If the first digit of N is in D, we write that digit and continue. For example, if N = 25123, then we will write 2 and continue.

If the first digit of N is larger than min(D), then we write the largest possible number from D less than that digit, and the rest of the numbers will be big. For example, if N = 5123, then we will write 4888 (4 then 888).

If the first digit of N is smaller than min(D), then we must "subtract 1" (in terms of X's bijective-base-B representation), and the rest of the numbers will be big.

For example, if N = 123, we will write 88. If N = 4123, we will write 2888. And if N = 22123, we will write 8888. This is because "subtracting 1" from '', '4', '22' yields '', '2', '8' (can't go below 0).

Actually, in our solution, it is easier to write in bijective-base-B, so instead of writing digits of D, we'll write the index of those digits (1-indexed). For example, X = 24888 will be A = [1, 2, 4, 4, 4]. Afterwards, we convert this to decimal.
'''
class Solution(object):
    def atMostNGivenDigitSet(self, D, N):
        B = len(D) # bijective-base B
        S = str(N)
        K = len(S)
        A = []  #  The largest valid number in bijective-base-B.

        for c in S:
            if c in D:
                A.append(D.index(c) + 1)
            else:
                i = bisect.bisect(D, c)
                A.append(i)
                # i = 1 + (largest index j with c >= D[j], or -1 if impossible)
                if i == 0:
                    # subtract 1
                    for j in range(len(A) - 1, 0, -1):
                        if A[j]: break
                        A[j] += B
                        A[j-1] -= 1

                A.extend([B] * (K - len(A)))
                break

        ans = 0
        for x in A:
            ans = ans * B + x
        return ans