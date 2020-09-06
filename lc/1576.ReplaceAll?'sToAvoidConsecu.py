# 1576. Replace All ?'s to Avoid Consecutive Repeating Characters
# Easy

# 16

# 33

# Add to List

# Share
# Given a string s containing only lower case English letters and the '?' character, convert all the '?' characters into lower case letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters.

# It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

# Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.

 

# Example 1:

# Input: s = "?zs"
# Output: "azs"
# Explanation: There are 25 solutions for this problem. From "azs" to "yzs", all are valid. Only "z" is an invalid modification as the string will consist of consecutive repeating characters in "zzs".
# Example 2:

# Input: s = "ubv?w"
# Output: "ubvaw"
# Explanation: There are 24 solutions for this problem. Only "v" and "w" are invalid modifications as the strings will consist of consecutive repeating characters in "ubvvw" and "ubvww".
# Example 3:

# Input: s = "j?qg??b"
# Output: "jaqgacb"
# Example 4:

# Input: s = "??yw?ipkj?"
# Output: "acywaipkja"
 

# Constraints:

# 1 <= s.length <= 100

# s contains only lower case English letters and '?'.



# THIS SOLUTION WORKS ! 

import random
class Solution:
    def modifyString(self, s: str) -> str:
        chars = 'abcdefghijklmnopqrstuvwxyz'
        ans = ""
        avoid = []
        '''
        make a tuple with start and end 
        start is before ? 
        end is after ?
        '''
        s_list = list(s)
        start = end = 0
        for start in range(len(s_list)):
            if s_list[start] =="?":
                end = start
                while end<len(s_list) and s_list[end] == "?":
                    end+=1
                avoid.append((start,end))

        for start, end in avoid:
            for i in range(start,end):
                idx = 0
                while (start != 0 and chars[idx] == s_list[start-1])  or (end<len(s_list) and chars[idx] == s_list[end]):  
                    idx = random.randint(0,25)
                s_list[i] = chars[idx] 
        return "".join(s_list)
   