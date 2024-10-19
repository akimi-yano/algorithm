'''
1545. Find Kth Bit in Nth Binary String
Solved
Medium
Topics
Companies
Hint
Given two positive integers n and k, the binary string Sn is formed as follows:

S1 = "0"
Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

For example, the first four strings in the above sequence are:

S1 = "0"
S2 = "011"
S3 = "0111001"
S4 = "011100110110001"
Return the kth bit in Sn. It is guaranteed that k is valid for the given n.

 

Example 1:

Input: n = 3, k = 1
Output: "0"
Explanation: S3 is "0111001".
The 1st bit is "0".
Example 2:

Input: n = 4, k = 11
Output: "1"
Explanation: S4 is "011100110110001".
The 11th bit is "1".
 

Constraints:

1 <= n <= 20
1 <= k <= 2n - 1
'''

class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def reverse(arr):
            left = 0 
            right = len(arr) - 1
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            return arr

        def invert(arr):
            for i in range(len(arr)):
                if arr[i] == "0":
                    arr[i] = "1"
                else:
                    arr[i] = "0"
            return arr

        dp = ["0"]
        for _ in range(n):
            if len(dp) == k:
                return dp[k-1]
            new_dp = dp + ["1"] +  reverse(invert(dp))
            dp = new_dp
        return dp[k-1]

# Another approach

class Solution:
    def reverse(arr):
        left = 0 
        right = len(arr) - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr

    def invert(arr):
        for i in range(len(arr)):
            if arr[i] == "0":
                arr[i] = "1"
            else:
                arr[i] = "0"
        return arr

    dp = ["0"]
    for _ in range(20):
        new_dp = dp + ["1"] +  reverse(invert(dp))
        dp = new_dp

    def findKthBit(self, n: int, k: int) -> str:
        return Solution.dp[k-1]


# Another approach

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        dp = [0]
        for i in range(n-1, -1, -1):
            dp.extend([1] + [1 ^ bit for bit in reversed(dp)])
        return str(dp[k-1])