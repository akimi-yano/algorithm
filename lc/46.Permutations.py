# 46. Permutations
def permute(nums):
    def helper(ns):
        temp = []
        if len(ns)==1:
            return [ns]
        for i in range(len(ns)):
            for arr in helper(ns[:i]+ns[i+1:]):    
                comb = [ns[i]]+arr
                temp.append(comb)
        return temp                
    return helper(nums)
print(permute([1]))
print(permute([1,2]))
print(permute([1,2,3]))
print(permute([1,2,3,4]))


        
        
        # if len(nums) == 1:
        #     return [nums[0]] 
        # comb = nums[0] + helper(nums[1:])
        # return comb

#         ans = []
#         def helper(i):
#             # if idx>len(nums)-1:
#             #     ans.append(temp)
#             #     return 
            
#             for k in range()
#             temp = [nums[i]+nums[:n]+nums[n+1:]]
            
#         for i in range(len(nums)):
#             # first = nums[i] 
#             # rest = nums[:i]+nums[i+1:]
#             helper(i)
#         return ans 
'''
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

3! - >3* 2! 

base case - > only one elem 
recursive - > n! = n * (n-1)!
loop the n and 

ex1
in: [1]
if len(nums) == 1:
return [1]

ex2
in: [1,2]
out - > [1,2] and [2,1]
if len(nums) == 1:
    return [nums[0]] 

comb = nums[0] + helper(nums[1:])
return comb


ex3
in: [1,2,3]

comb = nums[0] + helper(nums[1:])

for i in range(len(nums)):
    comb = nums[i]+helper(nums[:nums]+nums[nums+1:])


'''
