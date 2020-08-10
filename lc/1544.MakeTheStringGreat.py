# 1544. Make The String Great
# Easy

# 49

# 12

# Add to List

# Share
# Given a string s of lower and upper case English letters.

# A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

# 0 <= i <= s.length - 2
# s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
# To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

# Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

# Notice that an empty string is also good.

 

# Example 1:

# Input: s = "leEeetcode"
# Output: "leetcode"
# Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".
# Example 2:

# Input: s = "abBAcC"
# Output: ""
# Explanation: We have many possible scenarios, and all lead to the same answer. For example:
# "abBAcC" --> "aAcC" --> "cC" --> ""
# "abBAcC" --> "abBA" --> "aA" --> ""
# Example 3:

# Input: s = "s"
# Output: "s"
 

# Constraints:

# 1 <= s.length <= 100
# s contains only lower and upper case English letters.


# this solution works but really bad ...
class Solution:
    def makeGood(self, s: str) -> str:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        memo = {}
        for char in alpha:
            memo[char]=char.upper()
        # print(memo)

        s_list = list(s)
        # print(s_list)
        repeat=1
        while repeat > 0:
            i=0
            while i<len(s_list)-1:
                if (s_list[i] in memo and s_list[i+1] == memo[s_list[i]]) or (s_list[i+1] in memo and s_list[i] == memo[s_list[i+1]]):
                    s_list[i]=""
                    s_list[i+1]=""
                    repeat+=1
                else:
                    i+=1
            repeat-=1
            s="".join(s_list)
            s_list=list(s)
        return "".join(s_list)
        

# this soliution works and clean   !!!!!! :

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            elif stack[-1] != c and stack[-1].lower() == c.lower():
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)