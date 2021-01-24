# 1735. Count Ways to Make Array With Product
# Hard

# 41

# 12

# Add to List

# Share
# You are given a 2D integer array, queries. For each queries[i], where queries[i] = [ni, ki], find the number of different ways you can place positive integers into an array of size ni such that the product of the integers is ki. As the number of ways may be too large, the answer to the ith query is the number of ways modulo 109 + 7.

# Return an integer array answer where answer.length == queries.length, and answer[i] is the answer to the ith query.

 

# Example 1:

# Input: queries = [[2,6],[5,1],[73,660]]
# Output: [4,1,50734910]
# Explanation: Each query is independent.
# [2,6]: There are 4 ways to fill an array of size 2 that multiply to 6: [1,6], [2,3], [3,2], [6,1].
# [5,1]: There is 1 way to fill an array of size 5 that multiply to 1: [1,1,1,1,1].
# [73,660]: There are 1050734917 ways to fill an array of size 73 that multiply to 660. 1050734917 modulo 109 + 7 = 50734910.
# Example 2:

# Input: queries = [[1,1],[2,2],[3,3],[4,4],[5,5]]
# Output: [1,2,3,10,5]
 

# Constraints:

# 1 <= queries.length <= 104
# 1 <= ni, ki <= 104

# This solution works:
class Solution:
    MAX = 10000
    MOD = 10**9 + 7
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        primes = self.setup_primes()
        
        ans = []
        for n, k in queries:
            factors = self.factors(primes, k)
            
            perms = 1
            for num, count in factors.items():
                perms *= math.comb(n-1+count, count)
                perms %= Solution.MOD
            ans.append(perms)
        return ans
    
    @lru_cache(None)
    def setup_primes(self):
        primes = []
        not_primes = set([])

        for num in range(2, Solution.MAX+1):
            if num in not_primes:
                continue
            primes.append(num)
            cur = num
            while cur <= Solution.MAX:
                not_primes.add(cur)
                cur += num
        return primes
    
    def factors(self, primes, k):
        facs = {}
        for prime in primes:
            while k % prime == 0:
                if prime not in facs:
                    facs[prime] = 0
                facs[prime] += 1
                k //= prime
            if prime > k:
                break
        return facs
        