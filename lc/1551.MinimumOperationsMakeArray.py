# 1551. Minimum Operations to Make Array Equal

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


# This  works ! - cleaned up version is  below:
class Solution:
    def minOperations(self, n: int) -> int:
        if n %2 !=0:
            idx = (n-1)//2
            target = (2 * idx) + 1
            # s = (2 * 0) + 1
            
            def helper(s,e,target):
                s = (2 * s) + 1
                e = (2 * e) + 1
                count = 0
                while s<target<e:
                    # print(s,e)
                    s+=1
                    e-=1
                    count+=1
                return count
            
            count = 0
            for i in range(n//2):
                # count+=helper(i,n-1-i,target)
                count+=1*(((2 * (n-1-i)) + 1)-target)
                # print(count)
            return count
        
        
        else:
            def helper(s,e):
                s = (2 * s) + 1
                e = (2 * e) + 1
                count = 0
                while s<e:
                    # print(s,e)
                    s+=1
                    e-=1
                    count+=1
                return count
            
            count = 0
            for i in range(n//2):
                # count+=helper(i,n-1-i)
                count+=1*((((2 * (n-1-i)) + 1)-((2 * (i)) + 1))//2)
                # print(count)
            return count
#     1
#     r: 0
    
#     2
    
#     2 2 
#     1 3
#     [0,0]
#      0 1
        
#      4
#     [1 3 5 7]
#      0 1 2 3
        
#     1 7
    
#     2 6
#     3 5
#     4 4
        
        
#      1 3 5 7 9 11
#     [0,0,0,0,0,0]
#      0 1 2 3 4 5 
        
#     2 4 6 8 10 12
#     3 5 7 7 9 11
#     4 6 8 6 8 10
#     5 7 9 5 7 9
#     6 8   6 


# 1 11 3 9 5 7  

# 2 10 4 8 6 6 
# 3 9  5 7 
# 4 8  6 6
# 5 7
# 6 6

    
#             y2     x4
#      arr = [1, 3, 5]
# First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
# In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].



# cleaned up version  - there still migh be a better way :

class Solution:
    def minOperations(self, n: int) -> int:
        count = 0
        if n %2 !=0:
            idx = (n-1)//2
            target = (2 * idx) + 1
            for i in range(n//2):
                count+=1*(((2 * (n-1-i)) + 1)-target)
        else:     
            for i in range(n//2):
                count+=1*((((2 * (n-1-i)) + 1)-((2 * (i)) + 1))//2)
        return count
    
    
# another solution 

class Solution:
	def minOperations(self, n: int) -> int:
		arr = [2 * i + 1 for i in range(n)]
		target = sum(arr) // n
		res = 0
		for i in range(n // 2):
			res += target - arr[i]
		return res