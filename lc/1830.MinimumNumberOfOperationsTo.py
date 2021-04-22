# 1830. Minimum Number of Operations to Make String Sorted
# Hard

# 70

# 63

# Add to List

# Share
# You are given a string s (0-indexed)​​​​​​. You are asked to perform the following operation on s​​​​​​ until you get a sorted string:

# Find the largest index i such that 1 <= i < s.length and s[i] < s[i - 1].
# Find the largest index j such that i <= j < s.length and s[k] < s[i - 1] for all the possible values of k in the range [i, j] inclusive.
# Swap the two characters at indices i - 1​​​​ and j​​​​​.
# Reverse the suffix starting at index i​​​​​​.
# Return the number of operations needed to make the string sorted. Since the answer can be too large, return it modulo 109 + 7.

 

# Example 1:

# Input: s = "cba"
# Output: 5
# Explanation: The simulation goes as follows:
# Operation 1: i=2, j=2. Swap s[1] and s[2] to get s="cab", then reverse the suffix starting at 2. Now, s="cab".
# Operation 2: i=1, j=2. Swap s[0] and s[2] to get s="bac", then reverse the suffix starting at 1. Now, s="bca".
# Operation 3: i=2, j=2. Swap s[1] and s[2] to get s="bac", then reverse the suffix starting at 2. Now, s="bac".
# Operation 4: i=1, j=1. Swap s[0] and s[1] to get s="abc", then reverse the suffix starting at 1. Now, s="acb".
# Operation 5: i=2, j=2. Swap s[1] and s[2] to get s="abc", then reverse the suffix starting at 2. Now, s="abc".
# Example 2:

# Input: s = "aabaa"
# Output: 2
# Explanation: The simulation goes as follows:
# Operation 1: i=3, j=4. Swap s[2] and s[4] to get s="aaaab", then reverse the substring starting at 3. Now, s="aaaba".
# Operation 2: i=4, j=4. Swap s[3] and s[4] to get s="aaaab", then reverse the substring starting at 4. Now, s="aaaab".
# Example 3:

# Input: s = "cdbea"
# Output: 63
# Example 4:

# Input: s = "leetcodeleetcodeleetcode"
# Output: 982157772
 

# Constraints:

# 1 <= s.length <= 3000
# s​​​​​​ consists only of lowercase English letters.

# This solution works:

class Solution:
    MOD = 10 ** 9 + 7
    def makeStringSorted(self, s: str) -> int:
        '''
        basically check from bqxk qnd swap or not swap when I see smaller ones on the right
        use inverse factorial to keep the numbers small
        instead of doing division like this, use power to get an inverse factorial and simply multiply by the total factorial
        5!
        ---
        2!3!
        '''
        N = len(s)
        factorial = [0] * N
        inverse_factorial = [0] * N
        factorial[0] = 1
        inverse_factorial[0] = pow(1, Solution.MOD - 2, Solution.MOD)
        
        for i in range(1, N):
            factorial[i] = (i * factorial[i-1]) % Solution.MOD
            inverse_factorial[i] = pow(factorial[i], Solution.MOD-2, Solution.MOD)
        
        counts = [0] * 26
        ans = 0
        total = 0
        
        for c in s[::-1]:
            num = ord(c) - ord('a')
            counts[num] += 1
            
            for i in range(num):
                
                #there is a letter on the right side that is smaller than the current one
                if counts[i] > 0:
                    
                    # swap
                    counts[i] -= 1
                    
                    #total factorial
                    ops = factorial[total]
                    
                    # find the count for each letters
                    for j in range(26):
                        if counts[j] > 0:
                            ops = (ops * inverse_factorial[counts[j]]) % Solution.MOD
                    ans = (ans + ops) % Solution.MOD
                    counts[i] += 1
            total += 1
        
        return ans % Solution.MOD