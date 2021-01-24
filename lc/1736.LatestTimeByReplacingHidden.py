# 1736. Latest Time by Replacing Hidden Digits
# Easy

# 36

# 18

# Add to List

# Share
# You are given a string time in the form of hh:mm, where some of the digits in the string are hidden (represented by ?).

# The valid times are those inclusively between 00:00 and 23:59.

# Return the latest valid time you can get from time by replacing the hidden digits.

 

# Example 1:

# Input: time = "2?:?0"
# Output: "23:50"
# Explanation: The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.
# Example 2:

# Input: time = "0?:3?"
# Output: "09:39"
# Example 3:

# Input: time = "1?:22"
# Output: "19:22"
 

# Constraints:

# time is in the format hh:mm.
# It is guaranteed that you can produce a valid time from the given string.

# This solution works:

class Solution:
    def maximumTime(self, time: str) -> str:
        # 00:00 and 23:59
        times = time.split(":")
        hours = times[0] # 00 - 23
        mins = times[1] # 00 - 59
        
        ans_hours = ''
        if hours[0] == '?' and hours[1] == '?':
            ans_hours = "23"
        elif hours[0] == '?':
            for i in range(9, -1, -1):
                num = i*10 + int(hours[1])
                if 0 <= num < 24:
                    ans_hours = str(num)
                    break
        elif hours[1] == '?':
            for i in range(9, -1, -1):
                num = int(hours[0]) * 10 + i
                if 0 <= num < 24:
                    ans_hours = str(num)
                    break
        else:
            ans_hours = hours
        
        ans_mins = ''
        if mins[0] == '?' and mins[1] == '?':
            ans_mins = "59"
        elif mins[0] == '?':
            for i in range(9, -1, -1):
                num = i*10 + int(mins[1])
                if 0 <= num < 60:
                    ans_mins = str(num)
                    break
        elif mins[1] == '?':
            for i in range(9, -1, -1):
                num = int(mins[0]) * 10 + i
                if 0 <= num < 60:
                    ans_mins = str(num)
                    break
        else:
            ans_mins = mins
            
        return ans_hours.zfill(2) + ":" + ans_mins.zfill(2)