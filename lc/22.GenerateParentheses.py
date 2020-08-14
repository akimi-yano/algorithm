# 22. Generate Parentheses

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

# yay did it ! this worked !

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        o = n
        c = n 
        self.res = [] 
        def helper(s,o,c):
            if o<=0 and c<=0:
                self.res.append(s)
                return
            if o:
                helper(s+"(",o-1,c)
            if c and o<c:
                helper(s+")",o,c-1)
            
        helper("",o,c)
        return self.res 
    

# other solutions:
'''
p is the parenthesis-string built so far, left and right tell the number of left and right parentheses still to add, 
and parens collects the parentheses.

Solution 1

I used a few "tricks"... how many can you find?

'''

def generateParenthesis(self, n):
    def generate(p, left, right, parens=[]):
        if left:         generate(p + '(', left-1, right)
        if right > left: generate(p + ')', left, right-1)
        if not right:    parens += p,
        return parens
    return generate('', n, n)

'''
Solution 2

Here I wrote an actual Python generator. 
I allow myself to put the yield q at the end of the line because it's not that bad and because in "real life" I use Python 3 
where I just say yield from generate(...).

'''

def generateParenthesis(self, n):
    def generate(p, left, right):
        if right >= left >= 0:
            if not right:
                yield p
            for q in generate(p + '(', left-1, right): yield q
            for q in generate(p + ')', left, right-1): yield q
    return list(generate('', n, n))

'''
Solution 3

Improved version of this. Parameter open tells the number of "already opened" parentheses, and I continue the recursion as 
long as I still have to open parentheses (n > 0) and I haven't made a mistake yet (open >= 0).

'''

def generateParenthesis(self, n, open=0):
    if n > 0 <= open:
        return ['(' + p for p in self.generateParenthesis(n-1, open+1)] + \
               [')' + p for p in self.generateParenthesis(n, open-1)]
    return [')' * open] * (not n)


# DP Solution 

'''
To generate all n-pair parentheses, we can do the following:

Generate one pair: ()

Generate 0 pair inside, n - 1 afterward: () (...)...

Generate 1 pair inside, n - 2 afterward: (()) (...)...

...

Generate n - 1 pair inside, 0 afterward: ((...))

I bet you see the overlapping subproblems here. Here is the code:

(you could see in the code that x represents one j-pair solution and y represents one (i - j - 1) pair solution, 
and we are taking into account all possible of combinations of them)
'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]
    
    
    
# Simple Python DFS solution with explanation

'''
If you have two stacks, one for n "(", the other for n ")", you generate a binary tree from these two stacks of 
left/right parentheses to form an output string.

This means that whenever you traverse deeper, you pop one parentheses from one of stacks. When two stacks are empty, 
you form an output string.

How to form a legal string? Here is the simple observation:

For the output string to be right, stack of ")" most be larger than stack of "(". If not, it creates string like "())"
Since elements in each of stack are the same, we can simply express them with a number. For example, left = 3 is like 
a stacks ["(", "(", "("]
So, here is my sample code in Python:
'''

class Solution:
# @param {integer} n
# @return {string[]}
def generateParenthesis(self, n):
    if not n:
        return []
    left, right, ans = n, n, []
    self.dfs(left,right, ans, "")
    return ans

def dfs(self, left, right, ans, string):
    if right < left:
        return
    if not left and not right:
        ans.append(string)
        return
    if left:
        self.dfs(left-1, right, ans, string + "(")
    if right:
        self.dfs(left, right-1, ans, string + ")")