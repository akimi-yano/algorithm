# Eyeopening Algorithms & Data Structure Notes (LIBRARY)

# SHALLOW COPY VS DEEP COPY 

'''
shallow copy - updating one column will update the column for all the rows
'''
n=3
matrix=[[0]*n]*n
matrix[0][0]=1
print("Shallow Copy:",matrix)

'''
deep copy
'''
n=3 
matrix=[[0 for i in range (n)] for i in range(n)]
matrix[0][0]=1
print("Deep Copy:",matrix)

# RECURSION 
'''
IMPORTANT - its ok to not wrtite base case explicitly as long as the recursive call does not keep calling new new recursive stack
Sometimes you dont write a base case in the first line 
'''


# BINARY SEARCH 
'''
two ticks to avoid infinite loop
1) because of integer devision, mid will  be always smaller one, so  always move low (left = mid+1) but we dont necessarily move right.
ex. right=mid is ok the while loop condition is while left<right
2) or we can do the mid calculation like mid = (left+right+1)//2 to get the higher one so that we can do
right=mid-1 and left = mid  


this  approach is not to  find the answer  but to elminate all options that are not answers by divide and conquer
it will never bypass the answer because high =  mid when arr[mid]>= key (instead of high = mid -1) 
also  low = mid +1  when arr[mid]<key focusing on  the boundries than getting an answer


EX)
'''
def search_first_of_k(arr: List[int], key: int) -> int:
    if len(arr) < 1:
        return -1

    lo,hi = 0, len(arr)-1
    while lo<hi:
        mid = (lo+hi)//2
        if arr[mid] >= key:
            hi = mid
        else:
            lo = mid+1
    return -1 if arr[lo] != key else lo


# UNPACKING ARGUMENT LISTS

'''
use * to  spread / unpack array / arrays 
'''

a = [1, 2, 3]
a
[1, 2, 3]
def test(one, two, three):
    print(one)
    print(two)
    print(three)

test
# test(a)

test(*a)

b =[1, 2, 3, 4]
# test(b)
# test(*b)

import heapq

ab_list = [a, b]
print(list(heapq.merge(*ab_list)))