# 969. Pancake Sorting

# Given an array of integers A, We need to sort the array performing a series of pancake flips.

# In one pancake flip we do the following steps:

# Choose an integer k where 0 <= k < A.length.
# Reverse the sub-array A[0...k].
# For example, if A = [3,2,1,4] and we performed a pancake flip choosing k = 2, we reverse the sub-array [3,2,1], so A = [1,2,3,4] after the pancake flip at k = 2.

# Return an array of the k-values of the pancake flips that should be performed in order to sort A. Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.

# Example 1:

# Input: A = [3,2,4,1]
# Output: [4,2,4,3]
# Explanation: 
# We perform 4 pancake flips, with k values 4, 2, 4, and 3.
# Starting state: A = [3, 2, 4, 1]
# After 1st flip (k = 4): A = [1, 4, 2, 3]
# After 2nd flip (k = 2): A = [4, 1, 2, 3]
# After 3rd flip (k = 4): A = [3, 2, 1, 4]
# After 4th flip (k = 3): A = [1, 2, 3, 4], which is sorted.
# Notice that we return an array of the chosen k values of the pancake flips.
# Example 2:

# Input: A = [1,2,3]
# Output: []
# Explanation: The input is already sorted, so there is no need to flip anything.
# Note that other answers, such as [3, 3], would also be accepted.

# Constraints:

# 1 <= A.length <= 100
# 1 <= A[i] <= A.length
# All integers in A are unique (i.e. A is a permutation of the integers from 1 to A.length).





# First approach: recursion  - This does not work 


# Second approach while loop - This does not work 

# class Solution:
#     def pancakeSort(self, A: List[int]) -> List[int]:
#         '''
#         traverse from the end of the array 
#         if its not the largest, flip it with the beginning
#         flip it with the one at the spot
#         '''
        
#         i = len(A)-1
#         while i > -1:
#             k=i
#             target = i+1
#             while A[k]!=target:       
#                 k-=1
#             A = A[:k+1:-1]+A[k+1:]
#             print(A)
#             A = A[:i:-1]
#             i-=1
            


# This solution works !!!

class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        '''
        traverse from the end of the array 
        if its not the largest, flip it with the beginning
        flip it with the one at the spot
        '''
        
        i = len(A)-1
        answer = []
        while i > -1:
            k=i
            target = i+1
            
            while A[k]!=target:
                k-=1
            A = list(reversed(A[:k+1]))+A[k+1:]
            answer.append(k+1)
        
            A = list(reversed(A[:i+1])) +A[i+1:]
            answer.append(i+1)
            i-=1
        return answer