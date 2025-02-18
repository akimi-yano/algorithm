'''
2375. Construct Smallest Number From DI String
Medium
Topics
Companies
Hint
You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.

A 0-indexed string num of length n + 1 is created using the following conditions:

num consists of the digits '1' to '9', where each digit is used at most once.
If pattern[i] == 'I', then num[i] < num[i + 1].
If pattern[i] == 'D', then num[i] > num[i + 1].
Return the lexicographically smallest possible string num that meets the conditions.

 

Example 1:

Input: pattern = "IIIDIDDD"
Output: "123549876"
Explanation:
At indices 0, 1, 2, and 4 we must have that num[i] < num[i+1].
At indices 3, 5, 6, and 7 we must have that num[i] > num[i+1].
Some possible values of num are "245639871", "135749862", and "123849765".
It can be proven that "123549876" is the smallest possible num that meets the conditions.
Note that "123414321" is not possible because the digit '1' is used more than once.
Example 2:

Input: pattern = "DDD"
Output: "4321"
Explanation:
Some possible values of num are "9876", "7321", and "8742".
It can be proven that "4321" is the smallest possible num that meets the conditions.
 

Constraints:

1 <= pattern.length <= 8
pattern consists of only the letters 'I' and 'D'.
'''

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        def helper(i, prev, seen, all):
            if i > len(pattern)-1:
                ans.append(all)
                return

            if pattern[i] == 'I':
                for next_num in range(prev+1, 10):
                    if next_num in seen:
                        continue
                    seen.add(next_num)
                    helper(i+1, next_num, seen, all+[next_num])
                    seen.remove(next_num)
            else:
                for next_num in range(1, prev):
                    if next_num in seen:
                        continue
                    seen.add(next_num)
                    helper(i+1, next_num, seen, all+[next_num])
                    seen.remove(next_num)
        
        ans = []
        seen = set([])
        for num in range(1, 10):
            seen.add(num)
            helper(0, num, seen, [num])
            seen.remove(num)
        return "".join(str(elem) for elem in sorted(ans)[0])
    
# Another way:

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # Reverse all numbers between "I".
        res, stack = [], []
        for i,c in enumerate(pattern + 'I', 1):
            stack.append(str(i))
            if c == 'I':
                res += stack[::-1]
                stack = []
        return ''.join(res)