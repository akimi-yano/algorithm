# 282. Expression Add Operators
# Hard

# 2066

# 351

# Add to List

# Share
# Given a string num that contains only digits and an integer target, return all possibilities to add the binary operators '+', '-', or '*' between the digits of num so that the resultant expression evaluates to the target value.

 

# Example 1:

# Input: num = "123", target = 6
# Output: ["1*2*3","1+2+3"]
# Example 2:

# Input: num = "232", target = 8
# Output: ["2*3+2","2+3*2"]
# Example 3:

# Input: num = "105", target = 5
# Output: ["1*0+5","10-5"]
# Example 4:

# Input: num = "00", target = 0
# Output: ["0*0","0+0","0-0"]
# Example 5:

# Input: num = "3456237490", target = 9191
# Output: []
 

# Constraints:

# 1 <= num.length <= 10
# num consists of only digits.
# -231 <= target <= 231 - 1


# This solution works:


'''
Quite diffucult problem, which is similar to Basic Calculators problem (0224, 0227). Let us consider dfs with the following parameters:

idx is the index of current element we traverse in num.
path is the string built so far.
value is current value of created path.
last is the value of the last monomial.
Here we use idea of stack of monomials: imagine, that we have expression 1*2 + 3*4*5, then we have the following steps: [1], [2], [2, 3], [2,12], [2,60]: each time we have + or - we add one element to the end of stack; each time we have * we update the last element in stack.

Then when we traverse our string, we can have several options: each time we need to create tmp = int(num[idx: i]) and make sure that this is valid number: tmp will be the next number we are going to use. Then if last == None, we have only one option. If last != None, we can have 3 options which symbol we can take: if it is + or -, we just update value and sign of tmp. If it is multiplication, we need to update both value and last should be multiplied by tmp.

Complexity
It is potentially O(4^n * n), because on each step we have 4 options: +, -, * or no sign. Space complexity potentially the same.
'''
class Solution:
    def addOperators(self, num, target):
        def dfs(idx, path, value, last):            
            if idx == n and value == target:
                ans.append(path)
            
            for i in range(idx + 1, n + 1):
                tmp = int(num[idx: i])
                if i == idx + 1 or (i > idx + 1 and num[idx] != "0"):
                    if last is None :
                        dfs(i, num[idx: i], tmp, tmp)
                    else:
                        dfs(i, path + '+' + num[idx: i], value + tmp, tmp)
                        dfs(i, path + '-' + num[idx: i], value - tmp, -tmp)
                        dfs(i, path + '*' + num[idx: i], value - last + last*tmp, last*tmp)
        
        ans, n = [], len(num)
        dfs(0, "", 0, None)
        return ans