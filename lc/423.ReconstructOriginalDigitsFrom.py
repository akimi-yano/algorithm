# 423. Reconstruct Original Digits from English
# Medium

# 302

# 921

# Add to List

# Share
# Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

# Note:
# Input contains only lowercase English letters.
# Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
# Input length is less than 50,000.
# Example 1:
# Input: "owoztneoer"

# Output: "012"
# Example 2:
# Input: "fviefuro"

# Output: "45"

# This solution works:
from collections import Counter
class Solution:
    def originalDigits(self, s: str) -> str:
        digit_tuples = [
            (0, Counter('zero')),  # z
            (2, Counter('two')),   # w
            (4, Counter('four')),  # u
            (6, Counter('six')),   # x
            (8, Counter('eight')), # g
            (1, Counter('one')),   # o
            (3, Counter('three')), # h
            (5, Counter('five')),  # f
            (7, Counter('seven')), # v
            (9, Counter('nine'))   # n etc.
        ]
        chars_available = Counter(s)
        
        # {0: 1, 2: 2, 3: 4}
        digit_counts = {i: 0 for i in range(10)}
        for digit, chars_needed in digit_tuples:
            works = True
            while works:
                for c in chars_needed:
                    if chars_available[c] < chars_needed[c]:
                        works = False
                        break
                if works:
                    digit_counts[digit] += 1
                    for c in chars_needed:
                        chars_available[c] -= chars_needed[c]
                    
        
        ans_strs = []
        for digit in range(10):
            # ['0', '22', '3333']
            ans_strs.append(str(digit) * digit_counts[digit])
        return ''.join(ans_strs)