# 1551. Minimum Operations to Make Array Equal
# Medium

# 369

# 75

# Add to List

# Share
# You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid values of i (i.e. 0 <= i < n).

# In one operation, you can select two indices x and y where 0 <= x, y < n and subtract 1 from arr[x] and add 1 to arr[y] (i.e. perform arr[x] -=1 and arr[y] += 1). The goal is to make all the elements of the array equal. It is guaranteed that all the elements of the array can be made equal using some operations.

# Given an integer n, the length of the array. Return the minimum number of operations needed to make all the elements of arr equal.

 

# Example 1:

# Input: n = 3
# Output: 2
# Explanation: arr = [1, 3, 5]
# First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
# In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].
# Example 2:

# Input: n = 6
# Output: 9
 

# Constraints:

# 1 <= n <= 10^4

# This solution works:

class Solution:
    def minOperations(self, n: int) -> int:
        '''
        [1, 3, 5, 7, 9, 11]
        [2, 3, 5, 7, 9, 10]
        [3, 3, 5, 7, 9, 9]
        [4, 3, 5, 7, 9, 8]
        [5, 3, 5, 7, 9, 7]
        [6, 3, 5, 7, 9, 6]
        [6, 4, 5, 6, 9, 6]
        [6, 5, 5, 6, 8, 6]
        [6, 6, 5, 6, 7, 6]
        [6, 6, 6, 6, 6, 6]
        6-1 = 5
        6-3 = 3
        6-5 = 1
        7-6 = 1
        9-6 = 3
        11-6 = 5
        18//2 = 9
        '''
        arr = [(2 * i) + 1 for i in range(n)]
        ans = 0
        for num in arr:
            ans += abs(n-num)
        return ans//2


# This solution works - 1 liner:

class Solution:
    def minOperations(self, n: int) -> int:
        return sum([abs(n-((2*i)+1)) for i in range(n)])//2




# This solution works ! optimization with math formula of constant time complexity:

class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2 == 0:
            return (n//2)**2
        else:
            return (n//2)*((n//2)+1)

        '''
        n = 4
        1  3  5  7
        
        -3 -1 +1 +3
        
        1+3+5+ ... = ans
        (2-1)+(4-1)+(6-1)
        =(2+4+6...+n) - (1+1+1...) 
        =(n)(n+1) - n
        =1+2+...+n=(n)(n+1) // 2
        = n**2
        
        ______________________________
        n = 5
        1  3  5  7  9
        
        4  2  0 -2 -4
        
        (1+1)+(2+2)+(3+3)+(n+n)
        =2(1)+2(2)+2(3)+...2(n)
        =2*(1+2+3+4+...+n)
        =2*((n*(n+1))//2)
        =n*(n+1)
        
        
        '''