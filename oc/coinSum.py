# Complete the 'coinSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY coins
#  2. INTEGER total
#

# bruteforce
# memorization
# tabulation

def coinSum(coins, total):
    memo = {}
    def helper(n, i):
        if memo[coins[i]]:
            return memo[coins[i]]
        if n == coins[i]:
            return coins[i]
        ans = set([])
        if i > len(coins):
            ans.add(memo)
            return ans
        memo[coins[i]] = helper(coins[i],i+1)+helper(coins[i],i+1)+helper(coins[i],i+1)
        return memo[coins[i]]
    ans = helper(0,0)
    return len(list(ans))
    return helper()

