# 1864. Minimum Number of Swaps to Make the Binary String Alternating
# Medium

# 92

# 15

# Add to List

# Share
# Given a binary string s, return the minimum number of character swaps to make it alternating, or -1 if it is impossible.

# The string is called alternating if no two adjacent characters are equal. For example, the strings "010" and "1010" are alternating, while the string "0100" is not.

# Any two characters may be swapped, even if they are not adjacent.

 

# Example 1:

# Input: s = "111000"
# Output: 1
# Explanation: Swap positions 1 and 4: "111000" -> "101010"
# The string is now alternating.
# Example 2:

# Input: s = "010"
# Output: 0
# Explanation: The string is already alternating, no swaps are needed.
# Example 3:

# Input: s = "1110"
# Output: -1
 

# Constraints:

# 1 <= s.length <= 1000
# s[i] is either '0' or '1'.


# This solution works: 

from collections import Counter
class Solution:
    def minSwaps(self, s: str) -> int:
        counts = Counter(s)
        num0 = counts['0']
        num1 = counts['1']
        if abs(num0-num1) >= 2:
            return -1
        
        nums = list(s)
        ans = 0
        if num0 > num1:
            for i in range(len(nums)):
                if i % 2 == 0:
                    if nums[i] == '0':
                        pass
                    else:
                        for j in range(i+1, len(nums)):
                            if nums[j] == '0' and j % 2 == 1:
                                nums[i], nums[j] = nums[j], nums[i]
                                ans += 1
                                break
                else:
                    if nums[i] == '1':
                        pass
                    else:
                        for j in range(i+1, len(nums)):
                            if nums[j] == '1' and j % 2 == 0:
                                nums[i], nums[j] = nums[j], nums[i]
                                ans += 1
                                break
        elif num1 > num0:
            for i in range(len(nums)):
                if i % 2 == 0:
                    if nums[i] == '1':
                        pass
                    else:
                        for j in range(i+1, len(nums)):
                            if nums[j] == '1' and j % 2 == 1:
                                nums[i], nums[j] = nums[j], nums[i]
                                ans += 1
                                break
                else:
                    if nums[i] == '0':
                        pass
                    else:
                        for j in range(i+1, len(nums)):
                            if nums[j] == '0' and j % 2 == 0:
                                nums[i], nums[j] = nums[j], nums[i]
                                ans += 1
                                break  
        else:
            try1 = 0
            temp = list(nums)
            for i in range(len(nums)):
                if i % 2 == 0:
                    if nums[i] == '0':
                        pass
                    else:
                        for j in range(i+1, len(nums)):
                            if nums[j] == '0' and j % 2 == 1:
                                nums[i], nums[j] = nums[j], nums[i]
                                try1 += 1
                                break
                else:
                    if nums[i] == '1':
                        pass
                    else:
                        for j in range(i+1, len(nums)):
                            if nums[j] == '1' and j % 2 == 0:
                                nums[i], nums[j] = nums[j], nums[i]
                                try1 += 1
                                break
            
            nums = temp
            try2 = 0
            for i in range(len(nums)):
                if i % 2 == 0:
                    if nums[i] == '1':
                        pass
                    else:
                        for j in range(i+1, len(nums)):
                            if nums[j] == '1' and j % 2 == 1:
                                nums[i], nums[j] = nums[j], nums[i]
                                try2 += 1
                                break
                else:
                    if nums[i] == '0':
                        pass
                    else:
                        for j in range(i+1, len(nums)):
                            if nums[j] == '0' and j % 2 == 0:
                                nums[i], nums[j] = nums[j], nums[i]
                                try2 += 1
                                break  
            ans = min(try1, try2)
            
        return ans