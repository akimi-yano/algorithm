# 952. Largest Component Size by Common Factor
# Hard

# 824

# 74

# Add to List

# Share
# You are given an integer array of unique positive integers nums. Consider the following graph:

# There are nums.length nodes, labeled nums[0] to nums[nums.length - 1],
# There is an undirected edge between nums[i] and nums[j] if nums[i] and nums[j] share a common factor greater than 1.
# Return the size of the largest connected component in the graph.

 

# Example 1:


# Input: nums = [4,6,15,35]
# Output: 4
# Example 2:


# Input: nums = [20,50,9,63]
# Output: 2
# Example 3:


# Input: nums = [2,3,6,7,4,12,21,39]
# Output: 8
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# 1 <= nums[i] <= 105
# All the values of nums are unique.


# This solution works:


from collections import Counter, defaultdict

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        '''
        1 to find the common factor, we find prime numbers for each number
        2 and if its same as other number, then its a common factor (larger than 1) so connect with graph
        3 travarse the graphs and return the max length
        '''
        primes_to_idxs = defaultdict(list)
        for i, num in enumerate(A):
            prime_factors = self.prime_factors(num)
            for prime in prime_factors:
                primes_to_idxs[prime].append(i)
        # print(primes_to_idxs)

        self.roots = [i for i in range(len(A))]
        for idxs in primes_to_idxs.values():
            self.update_roots(idxs)
        # run find one last time
        self.roots = [self.find(idx) for idx in range(len(self.roots))]
        return max(Counter(self.roots).values())
        
    def update_roots(self, idxs):
        for i in range(len(idxs) - 1):
            idx1, idx2 = idxs[i], idxs[i+1]
            idx1_root, idx2_root = self.find(idx1), self.find(idx2)
            self.roots[idx1_root] = idx2_root
    
    def find(self, idx):
        if self.roots[idx] != idx:
            self.roots[idx] = self.find(self.roots[idx])
        return self.roots[idx]
        
    
    def prime_factors(self, n):
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return self.prime_factors(n//i) | set([i])
        return set([n])
