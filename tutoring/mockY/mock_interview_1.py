def canJump(nums):
    memo = {}
    def helper(i):

        if i >= len(nums):
            return False
        if i==len(nums)-1:
            return True
        if nums[i]== 0:
            return False
        for k in range (i + nums[i], i, -1):
            if k in memo:
                return memo[k]
        
            if helper(k):
                memo[k] = True
                return memo[k] 
        memo[i] = False
        return memo[i]
    return helper(0)

print(canJump([2,3,1,1,4]))
# True

print(canJump([3,2,1,0,4]))
# False
