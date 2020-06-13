# 368. Largest Divisible Subset

# Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

# Si % Sj = 0 or Sj % Si = 0.

# If there are multiple solutions, return any subset is fine.

# Example 1:

# Input: [1,2,3]
# Output: [1,2] (of course, [1,3] will also be ok)
# Example 2:

# Input: [1,2,4,8]
# Output: [1,2,4,8]

# To optimize, only save index and size instead of making arrs
# sort and check from the end of arr if they are divisible by the elem of the right and find the largest in length 
def largestDivisibleSubset(nums):
    n = len(nums)
    ans = []
    if n == 0:
        return ans
    nums.sort()
    # next one is default -1 as the last is the biggest and cannot be devided by others
    next_idx = [-1]*n 
    # its 1 by defaut as it can be devided byitself
    sizes = [1]*n
    max_len = 1
    max_idx = 0
        
    # check reversely
    for i in range(n-1,-1,-1):
        j=i+1
        temp_max_len = 0
        temp_max_idx = i
        while j<n:
            if nums[j]%nums[i]==0 and sizes[j]>temp_max_len:
                # only chosse the index of the element whose length is biggest and use the index later
                temp_max_len = sizes[j]
                temp_max_idx = j
            j+=1
        # only if its divisible and found the longest one do below
        if temp_max_idx != i:
            # updating the size and next index to be saved
            sizes[i]+=sizes[temp_max_idx]
            next_idx[i]=temp_max_idx
            
            # update the global max
            # +1 is needed because you added yourself
            if temp_max_len+1>max_len:
                max_len = temp_max_len+1
                max_idx = i
    curr = max_idx
    while curr >=0:
        ans.append(nums[curr])
        curr=next_idx[curr]
    return ans

print(largestDivisibleSubset([1,2,3])) # [1,2] 
print(largestDivisibleSubset([1,2,4,8])) # [1,2,4,8]



