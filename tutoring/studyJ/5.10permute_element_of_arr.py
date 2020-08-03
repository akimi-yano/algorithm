# 5.10 permute the elements of an array

# with additional space: 
# Time - O(N)
# Space - O(N)

# needs optimization
# def permute(P,A):
#     ans = [0]*len(P)
#     for i in range(len(P)):
#         ans[P[i]]=A[i]
#     A = ans
#     return  A
        
# P=[2,0,1,3]
# A=['a','b','c','d']
# print(permute(P,A))

# this does not work
# def without_space(P,A):
#     i = 0
#     while i == P[i]:
#         i+=1
#     start = i
#     val = A[i]
#     while True:
#         temp_val = A[P[i]]
#         temp_idx = P[i]
#         A[temp_idx]=val
#         i=temp_idx
#         val=temp_val
#         if i == start:
#             break
#     return A
# P=[2,0,1,3]
# A=['a','b','c','d']
# print(without_space(P,A))

# solution - this works!
def apply_perm(perm,A):
    for i in range(len(A)):
        while perm[i]!=i:
            A[perm[i]],A[i]=A[i],A[perm[i]]
            perm[perm[i]],perm[i]=perm[i],perm[perm[i]]
    return A
P=[2,0,1,3]
A=['a','b','c','d']          
print(apply_perm(P,A))
