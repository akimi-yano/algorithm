# 974. Subarray Sums Divisible by K
# Medium

# 1018

# 74

# Add to List

# Share
# Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.


# Example 1:

# Input: A = [4,5,0,-2,-3,1], K = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by K = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

# Note:

# 1 <= A.length <= 30000
# -10000 <= A[i] <= 10000
# 2 <= K <= 10000



# TLEd approach ! only tests passed 38/73 
# class Solution:
#     def subarraysDivByK(self, A: List[int], K: int) -> int:
#         count = 0
#         for i in range(len(A)):
#             for j in range(i+1,len(A)+1):

#                 if sum(A[i:j]) % K == 0:
#                     count+=1
#         return count



'''

Solution
Approach 1: Prefix Sums and Counting
Intuition

As is typical with problems involving subarrays, we use prefix sums to add each subarray. Let P[i+1] = A[0] + A[1] + ... + A[i]. Then, each subarray can be written as P[j] - P[i] (for j > i). Thus, we have P[j] - P[i] equal to 0 modulo K, or equivalently P[i] and P[j] are the same value modulo K.

Algorithm

Count all the P[i]'s modulo K. Let's say there are C_xC x values P[i] \equiv x \pmod{K}P[i]≡x(modK). 
Then, there are \sum_x \binom{C_x}{2}∑ x( 2C x) possible subarrays.

For example, take A = [4,5,0,-2,-3,1] and K = 5. Then P = [0,4,9,9,7,4,5], and C_0 = 2, C_2 = 1, C_4 = 4C 0=2,C 2=1,C 4=4:

With C_0 = 2C 0=2 (at P[0]P[0], P[6]P[6]), it indicates \binom{2}{2} = 1( 22)=1 subarray with sum divisible by KK, namely A[0:6] = [4, 5, 0, -2, -3, 1]A[0:6]=[4,5,0,−2,−3,1].
With C_4 = 4C 4=4 (at P[1]P[1], P[2]P[2], P[3]P[3], P[5]P[5]), it indicates \binom{4}{2} = 6( 24)=6 subarrays with sum divisible by KK, namely A[1:2]A[1:2], A[1:3]A[1:3], A[1:5]A[1:5], A[2:3]A[2:3], A[2:5]A[2:5], A[3:5]A[3:5].


Complexity Analysis

Time Complexity: O(N)O(N), where NN is the length of A.

Space Complexity: O(N)O(N). (However, the solution can be modified to use O(K)O(K) space by storing only count.)

'''

class Solution(object):
    def subarraysDivByK(self, A, K):
        P = [0]
        for x in A:
            P.append((P[-1] + x) % K)

        count = collections.Counter(P)
        return sum(v*(v-1)/2 for v in count.values())
    
    
# I LIKE THIS SOLUTION ! ITS VERY INSTUITIVE !
'''
1 make a dictionary with prefix sum % K to count how many of them
2 iterate throught the array to update the target variable to find -> subtract by 1 because you are removing the elements from 
left of the sub arrays - keep adding the count to the answers

Its efficient because each operation is constant time
and linear iteration

Time: O(N)
Space: O(min(K,N))
'''

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        prefix = 0
        mod_counts = {}
        for elem in A:
            prefix = (prefix + elem) % K
            if prefix not in mod_counts:
                mod_counts[prefix] = 0
            mod_counts[prefix] += 1
        
        ans = 0
        mod_val = 0
        for elem in A:
            if mod_val in mod_counts:
                ans += mod_counts[mod_val]
            mod_val = (mod_val + elem) % K
            mod_counts[mod_val] -= 1
        return ans

'''
[4,5,0,-2,-3,1] K=5
[4,0,0,3,2,1] <- after %K

Remove the previous one and count the # of 0s!

 [4,4,4,2,4,0] +1 
-4 [0,0,3,0,1] +3
-0   [0,3,0,1] +2
-0     [3,0,1] +1
-3       [2,3] +0
-2         [1] +0

return total (1+3+2+1+0+0) = (7)
'''