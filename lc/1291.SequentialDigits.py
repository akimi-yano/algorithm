# 1291. Sequential Digits
# Medium

# 371

# 45

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


# This approach TLEd - does not work:

# class Solution:
#     def sequentialDigits(self, low: int, high: int) -> List[int]:
#         ans = []
        
#         low_str = str(low)
#         digit = len(low_str)
        
#         num = int(low_str[0])
#         start_num = 0
#         for _ in range(digit):
#             start_num *= 10
#             start_num += num
#             num+=1
#         # print(start_num)
        
#         if low > start_num:
#             new_num = 0
#             for i in range(digit):
#                 new_num+=((start_num%10)+1)*10**i
#                 start_num//=10
                
#             start_num = new_num
        
#         ans.append(start_num)
#         while start_num <= high:
#             new_num = 0
#             for i in range(digit):
#                 new_num+=((start_num%10)+1)*10**i
#                 start_num//=10
                
#             start_num = new_num
#             if start_num <= high:
#                 ans.append(start_num)
        
#         return ans
        
        
        
# THIS SOLUTION WORKS  !
'''
make all the patterns and append it to the ans arr if its within the range -> if it goes over -> return
if I think a solution is expensice, understand the constraint well ! In this case, there are not many patterns
'''


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        for digits in range(2, 10):
            # print("{} digits".format(digits))
            for start in range(1, 11-digits):
                # print("  start at {}".format(start))
                num_arr = [str(start + i) for i in range(digits)]
                # print("  number: {}".format(num_arr))
                num = int(''.join(num_arr))
                if num < low:
                    continue
                if low <= num <= high:
                    ans.append(num)
                else:
                    return ans
        return ans