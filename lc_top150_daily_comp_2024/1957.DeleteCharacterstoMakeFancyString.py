'''
1957. Delete Characters to Make Fancy String
Solved
Easy
Topics
Companies
Hint
A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.

 

Example 1:

Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".
Example 2:

Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".
Example 3:

Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".
 

Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters.
'''

class Solution:
    def makeFancyString(self, s: str) -> str:
        char = s[0]
        count = 1
        ans = [char]
        for i in range(1, len(s)):
            if s[i] != char:
                char = s[i]
                count = 1
                ans.append(char)
            else:
                count += 1
                if count < 3:
                    ans.append(char)
        return "".join(ans)

class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        for char in s:
            if len(stack) >= 2 and stack[-2] == stack[-1] == char:
                continue
            stack.append(char)
        return "".join(stack)