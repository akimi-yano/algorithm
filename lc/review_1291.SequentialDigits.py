# 1291. Sequential Digits
# Medium

# 878

# 67

# Add to List

# Share
# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

# Example 1:

# Input: low = 100, high = 300
# Output: [123,234]
# Example 2:

# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]
 

# Constraints:

# 10 <= low <= high <= 10^9


# This solution works:


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        all_nums = []
        low_digit = len(str(low))
        high_digit = len(str(high))
        for digit in range(low_digit, high_digit+1):
            for start_num in range(1, 10):
                temp = 0
                start_digit = 0
                for num in range(start_num, 10):
                    temp = temp*10+num
                    start_digit += 1
                    if start_digit == digit:
                        if len(str(temp)) == digit:
                            all_nums.append(temp)
                        break
        
        ans = []
        for num in all_nums:
            if low <= num <= high:
                ans.append(num)
        return ans