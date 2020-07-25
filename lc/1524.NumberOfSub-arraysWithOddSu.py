# 1524. Number of Sub-arrays With Odd Sum

# Given an array of integers arr. Return the number of sub-arrays with odd sum.

# As the answer may grow large, the answer must be computed modulo 10^9 + 7.

# Example 1:

# Input: arr = [1,3,5]
# Output: 4
# Explanation: All sub-arrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
# All sub-arrays sum are [1,4,9,3,8,5].
# Odd sums are [1,9,3,5] so the answer is 4.
# Example 2:

# Input: arr = [2,4,6]
# Output: 0
# Explanation: All sub-arrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
# All sub-arrays sum are [2,6,12,4,10,6].
# All sub-arrays have even sum and the answer is 0.
# Example 3:

# Input: arr = [1,2,3,4,5,6,7]
# Output: 16
# Example 4:

# Input: arr = [100,100,99,99]
# Output: 4
# Example 5:

# Input: arr = [7]
# Output: 1


# Constraints:

# 1 <= arr.length <= 10^5
# 1 <= arr[i] <= 100


# This does not work - see below for solution that works
# import math
# class Solution:
#     def numOfSubarrays(self, arr: List[int]) -> int:
#         odd = 0
#         n = len(arr)
#         for elem in arr:
#             if elem%2!=0:
#                 odd+=1
#         if odd ==0:
#             return 0
#         # print(odd)
#         total = math.factorial(odd+((n-odd)//2))
#         return total//2 +1
#         # ans = 0
#         # res = []
#         # for i in range(len(arr)):
#         #     temp = 0
#         #     for k in range(i,len(arr)):
#         #         temp+=arr[k]
#         #         res.append(temp)
#         # # print(res)
#         # for r in res:
#         #     if r % 2!=0:
#         #         ans+=1
#         # ans = ans % (10**9 + 7)
#         # return ans
#     # (num_odd !)//2+1







# DP Solution that works!


# This is an elementary dynamic programming problem.
# odd[i] records the number of subarray ending at arr[i] that has odd sum.
# even[i] records the number of subarray ending at arr[i] that has even sum.
# if arr[i + 1] is odd, odd[i + 1] = even[i] + 1 and even[i + 1] = odd[i]
# if arr[i + 1] is even, odd[i + 1] = odd[i] and even[i + 1] = even[i] + 1
# Since we only required the previous value in odd and even, we only need O(1) space.

# Please upvote if you find this post helpful or interesting. It means a lot to me. Thx~

# Complexity

# Time: O(n)
# Space: O(1)
# Python

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res = odd = even = 0
        for x in arr:
            even += 1
            if x % 2:
                odd, even = even, odd
            res = (res + odd) % 1000000007             
        return res            
    
    

# another approach from https://www.geeksforgeeks.org/number-of-subarrays-with-odd-sum/

# O(n) Time and O(1) Space Method [Efficient]
# If we do compute the cumulative sum array in temp[] of our input array, 
# then we can see that the sub-array starting from i and ending at j, 
# has an even sum if temp[] if (temp[j] – temp[i]) % 2 = 0. So, 
# instead of building a cumulative sum array we build a cumulative sum modulo 2 array. 
# Then calculating odd-even pairs will give the required result i.e. temp[0]*temp[1].

# Python 3 proggram to   
# find count of sub-arrays 
# with odd sum 
def countOddSum(ar, n): 
      
    # A temporary array of size  
    # 2. temp[0] is going to  
    # store count of even subarrays 
    # and temp[1] count of odd. 
    # temp[0] is initialized as 1  
    # because there is a single odd  
    # element is also counted as 
    # a subarray 
    temp = [ 1, 0 ] 
  
    # Initialize count. sum is sum  
    # of elements under modulo 2  
    # and ending with arr[i]. 
    result = 0
    val = 0
  
    # i'th iteration computes  
    # sum of arr[0..i] under  
    # modulo 2 and increments  
    # even/odd count according 
    # to sum's value 
    for i in range(n): 
          
        # 2 is added to handle 
        # negative numbers 
        val = ((val + ar[i]) % 2 + 2) % 2
  
        # Increment even/odd count 
        temp[val] += 1
  
    # An odd can be formed  
    # by even-odd pair 
    result = (temp[0] * temp[1]) 
  
    return (result) 
  
# Driver code 
ar = [ 5, 4, 4, 5, 1, 3 ] 
  
print("The Number of Subarrays"
           " with odd sum is "+
       str(countOddSum(ar, 6))) 
         
         
# Another approach!

# Explanation
# cur = 0 if current prefix sum is even
# cur = 1 if current prefix sum is odd
# count[0] is the number of even prefix sum
# count[1] is the number of odd prefix sum

# For each element in A:
# if current prefix sum is even, res += the number of odd prefix sum
# if current prefix sum is odd, res += the number of even prefix sum


# Complexity
# Time O(N)
# Space O(1)

    def numOfSubarrays(self, A):
        count = [1, 0]
        cur = res = 0
        for a in A:
            cur ^= a & 1
            res += count[1 - cur]
            count[cur] += 1
        return res % (10**9 + 7) 
    

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        
        """
        o:   0 -> 0 -> 0 -> 3 -> 3 -> 3
        e:   0 -> 1 -> 2 -> 0 -> 1 -> 2
        ans: 0 -> 0 -> 0 -> 3 -> 6 -> 9
                 [0,   0,   1,   0,   0]
        """

        # number of even subarrays ending at index (gets updated every for loop iteration)
        num_even = 0
        # number of odd subarrays ending at index (gets updated every for loop iteration)
        num_odd = 0
        ans = 0
        for elem in arr:
            # print(i, elem, num_even, num_odd)
            # even numbers don't change the subarray sum even/odd
            if elem % 2 == 0:
                ans = (ans + num_odd) % MOD
                num_even += 1
            else:
                ans = (ans + num_even + 1) % MOD
                num_even, num_odd = num_odd, num_even + 1
        return ans