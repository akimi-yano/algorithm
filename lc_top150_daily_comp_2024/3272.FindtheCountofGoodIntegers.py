'''
3272. Find the Count of Good Integers
Hard
Topics
Companies
Hint
You are given two positive integers n and k.

An integer x is called k-palindromic if:

x is a palindrome.
x is divisible by k.
An integer is called good if its digits can be rearranged to form a k-palindromic integer. For example, for k = 2, 2020 can be rearranged to form the k-palindromic integer 2002, whereas 1010 cannot be rearranged to form a k-palindromic integer.

Return the count of good integers containing n digits.

Note that any integer must not have leading zeros, neither before nor after rearrangement. For example, 1010 cannot be rearranged to form 101.

 

Example 1:

Input: n = 3, k = 5

Output: 27

Explanation:

Some of the good integers are:

551 because it can be rearranged to form 515.
525 because it is already k-palindromic.
Example 2:

Input: n = 1, k = 4

Output: 2

Explanation:

The two good integers are 4 and 8.

Example 3:

Input: n = 5, k = 6

Output: 2468

 

Constraints:

1 <= n <= 10
1 <= k <= 9
'''

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        half = (n + 1)//2 # example , n = 5 , half = 3
        res = 0
        seen = set()
        
        for v in range( 10**(half - 1), 10**(half)): # 100 -> 1000 ( 100 to 999)
            vv = str(v) + str(v)[::-1][n % 2:] # 233 + 32 = "23332", 109+ 01 = "10901"
            key = ''.join(sorted(vv))
            
            if int(vv) % k == 0 and key not in seen:
                seen.add(key)
                count = Counter(vv) # for finding the duplicates for "10901" {1:2, 0:2, 9:1}
                x = (n - count['0']) * factorial(n - 1)
                '''
                   10901 => first position cannot be 0 so (5 - 2)
                   Already placed one number on first position, so we can take remaining 4
                   so (5 - 2)*4*3*2*1 total permutations
                
                '''
                
                for i, c in count.items():
                    # Remove duplicates to handle repeated digits
                    x //= factorial(c)
                
                res += x
        return res