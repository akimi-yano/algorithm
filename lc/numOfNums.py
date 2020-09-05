def numOfWays(nums):
    mod = 1000000000 + 7
    N = len(nums)
    fact = [1]*(2*N)
    for index in range(1, len(fact)):
        fact[index] = (fact[index-1]* index)
    
    def c(left, right):
        return (fact[len(left)+len(right)] // fact[len(left)] // fact[len(right)]) % mod
    
    def go(arr):
        if len(arr) == 0:
            return 1
        if len(arr) == 1:
            return 1
        x = arr[0]
        left = [y for y in arr if y < x]
        right = [y for y in arr if y > x]
        return (go(left) % mod) * (go(right) % mod) * (c(left,right) % mod)
    return (go(nums)-1) % mod