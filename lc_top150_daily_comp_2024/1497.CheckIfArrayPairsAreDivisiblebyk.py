'''
1497. Check If Array Pairs Are Divisible by k
Solved
Medium
Topics
Companies
Hint
Given an array of integers arr of even length n and an integer k.

We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

Return true If you can find a way to do that or false otherwise.

 

Example 1:

Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
Output: true
Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
Example 2:

Input: arr = [1,2,3,4,5,6], k = 7
Output: true
Explanation: Pairs are (1,6),(2,5) and(3,4).
Example 3:

Input: arr = [1,2,3,4,5,6], k = 10
Output: false
Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.
 

Constraints:

arr.length == n
1 <= n <= 105
n is even.
-109 <= arr[i] <= 109
1 <= k <= 105
'''

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        '''
        - if two numbers remainders sum to k, their original sum will be divisible by k
        - special cases: when remainder is 0, as we need an even number of such elements, and
        when the remainder is exactly half of k, we need an even number of such elements.
        
        For negative number:
        remainder=(num%k+k)%k
        ^This ensures that for any negative number, the remainder will always be in the range [0, k-1], 
        just like for positive numbers.
        '''
        # Count the remainders when divided by k
        remainder_count = [0] * k

        for num in arr:
            # remainder of each elem is divisible by k, then sum of all is also divisible by k
            # handle negative numbers
            # Adjust the remainder to always be positive
            remainder = (num % k + k) % k
            remainder_count[remainder] += 1
        
        # For remainder 0, the count must be even
        if remainder_count[0] % 2 != 0:
            return False

        # For other remainders, remainder[i] should pair with remainder[k-i]
        for i in range(1, k):
            if i != k - i:  # For general cases
                if remainder_count[i] != remainder_count[k - i]:
                    return False
            else:  # Special case when k is even and i == k // 2
                if remainder_count[i] % 2 != 0:
                    return False
        
        return True

# Time: O(max(N, K))
# Space: O(K)