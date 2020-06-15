# [Completed]
# 5.1 The Dutch National Flag Problem

# goal:
# smaller | same | larger
# [0,0,1,1,1,2,2]

A = [0,1,2,0,2,1,1]
#new:0 0 1 1 1 2 2
    #            l
   #               r
# review the quicksort code from class

# def pivot_partition(A):
#     pivot = len(A)-1
#     val = A[pivot]
#     left = 0
#     right = len(A)-1
#     while left<len(A):
#         if A[left]<val:
#             left+=1   
#         else:
#             while right>-1 and A[right]>val:
#                 right-=1
#             if right>-1:
#                 A[left], A[right] = A[right], A[left]
#             left+=1
#     print(left,right)
#     return A
# print(pivot_partition(A))

# with extra storage
def extra_space(A):
    smaller = []
    larger = []
    same = []
    pivot = len(A)-1
    val = A[pivot]
    for a in A:
        # print(val,a)
        if a == val:
            same.append(a)
        elif a>val:
            larger.append(a)
        else:
            smaller.append(a)
    # print(smaller)
    # print(same)
    # print(larger)
    ans = smaller+same+larger
    return ans
print(extra_space(A))


# O(N) and O(1)
B = [0,1,2,0,2,1,1]
def improved(B):
    pivot = A[len(B)-1]
    
    # first path: group elements smaller than pivot
    smaller = 0
    for i in range(len(B)):
        if B[i]<pivot:
            B[i],B[smaller]=B[smaller],B[i]
            smaller+=1
        
    # second path: group elements larger than pivot
    larger = len(B)-1
    for k in reversed(range(len(B))):
        if B[k]>pivot:
            B[k],B[larger] = B[larger],B[k]
            larger-=1
    return B
print(improved(B))

C = [0,1,2,0,2,1,1]
# O(N) and O(1) faster solution
def faster(C):
    pivot = C[len(C)-1]
    
    # keep the following invariants during partitioning
    # bottom group : C[:smaller]
    # middle group : C[smaller:equal]
    # unclassified group : C[equal:larger]
    # top group : C[larger:]
    
    smaller,equal,larger = 0,0,len(C)
    # keep iterating as long as there is an unclassified element
    
    while equal<larger:
        # C[equal]is the incoming unclassified element
        if C[equal]<pivot:
            C[smaller],C[equal]=C[equal],C[smaller]
            smaller,equal = smaller+1,equal+1
        elif C[equal] == pivot:
            equal+=1
        else:
            #C[equal]>pivot
            larger-=1
            C[equal],C[larger]=C[larger],C[equal]
    return C
print(faster(C))