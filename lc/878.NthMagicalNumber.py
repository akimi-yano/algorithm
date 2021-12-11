# 878. Nth Magical Number
# Hard

# 385

# 84

# Add to List

# Share
# A positive integer is magical if it is divisible by either a or b.

# Given the three integers n, a, and b, return the nth magical number. Since the answer may be very large, return it modulo 109 + 7.

 

# Example 1:

# Input: n = 1, a = 2, b = 3
# Output: 2
# Example 2:

# Input: n = 4, a = 2, b = 3
# Output: 6
# Example 3:

# Input: n = 5, a = 2, b = 4
# Output: 10
# Example 4:

# Input: n = 3, a = 6, b = 4
# Output: 8
 

# Constraints:

# 1 <= n <= 109
# 2 <= a, b <= 4 * 104


# This solution works:


'''
Suppose A =2 and B = 3, then the lcm is 6. The list of magical number less or equal to 6 is [2,3,4,6]. Then, the 1st to 4th magical number to [2,3,4,6], the 5th to 8th number is 6 added to [2,3,4,6] respectively, the 9th to 12nd number is 6*2 added to [2,3,4,6] respectively, and so on.

So, the key here is to get all the magical number less or equal to the lcm of A and B. Then, the Nth number can be obtained immediately.
'''
class Solution(object):
	def gcd(self, x, y):
		while y > 0:
			x, y = y, x % y
		return x

	def lcm(self, x, y):
		return x*y//self.gcd(x,y)

	def nthMagicalNumber(self, N, A, B):
		temp = self.lcm(A,B)
		seq = {}
		for i in range(1,temp//A+1):
			seq[i*A] = 1
		for i in range(1,temp//B+1):
			seq[i*B] = 1
		cand = sorted([key for key, value in seq.items()])
		ans = ((N-1)//len(cand))*cand[-1] + cand[N%len(cand)-1]
		return ans % (10**9+7)