# 1542. Find Longest Awesome Substring
# User Accepted:313
# User Tried:1262
# Total Accepted:335
# Total Submissions:2833
# Difficulty:Hard
# Given a string s. An awesome substring is a non-empty substring of s such that we can make any number of swaps in order to make it palindrome.

# Return the length of the maximum length awesome substring of s.

 

# Example 1:

# Input: s = "3242415"
# Output: 5
# Explanation: "24241" is the longest awesome substring, we can form the palindrome "24142" with some swaps.
# Example 2:

# Input: s = "12345678"
# Output: 1
# Example 3:

# Input: s = "213123"
# Output: 6
# Explanation: "213123" is the longest awesome substring, we can form the palindrome "231132" with some swaps.
# Example 4:

# Input: s = "00"
# Output: 2
 

# Constraints:

# 1 <= s.length <= 10^5
# s consists only of digits.


# this solution works + explanation with all the printing statements !

class Solution:
    def longestAwesome(self, s: str) -> int:
        def bin_str(mask):
            return ''.join(list('0' * (6-len(bin(mask)[2:])) + bin(mask)[2:]))
    
        longest = 1
        mask = 0
        memo = {0: -1}

        for i, digit_char in enumerate(s):
            print("i={}, digit={}".format(i, digit_char))
            print("Mask before: {}".format(bin_str(mask)))
            digit = int(digit_char)
            mask ^= 1 << digit
            print("Mask  after: {}".format(bin_str(mask)))
            print("Mask Memo: {}".format([(bin_str(k), v) for k, v in memo.items()]))

            for odd_digit in range(-1, 10):
                adjusted_mask = mask
                # if -1, we assume character counts are all even
                if odd_digit == -1:
                    pass
                # else, set one of the character counts to odd
                else:
                    adjusted_mask = mask ^ (1 << odd_digit)
                if adjusted_mask in memo:
                    distance = i - memo[adjusted_mask]
                    if distance > longest:
                        print("   \n*Matched mask {} using {} {}\n".format(bin_str(adjusted_mask), "even" if odd_digit < 0 else "odd", "digit counts" if odd_digit < 0 else odd_digit))
                        longest = distance

            if mask not in memo:
                memo[mask] = i
                print("    New Mask: {}".format(bin_str(mask)))
            print("--------")
        return longest
    
    
print(Solution().longestAwesome("3242415"))