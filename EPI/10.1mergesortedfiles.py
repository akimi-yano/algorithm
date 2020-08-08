# 10.1 merge sorted files 

# merge K sorted arr problems 
# look at the first elem 
# use heap

# EXAMPLE:
# input:
# [3,5,7]
# [0,6]
# [0,6,28]

# output:
# [0,0,3,5,6,6,7,28]

# solution 1 - most intuitive - time: O(nlogk) and space: O(k)
import heapq
def merge_k_arr2(arrs):
    ans = []
    minheap = []
    for arr_i in range(len(arrs)):
        heapq.heappush(minheap,(arrs[arr_i][0],arr_i,0))

    while minheap:
        val,arr_i,idx=heapq.heappop(minheap)
        ans.append(val)
        next_idx = idx+1
        if next_idx<len(arrs[arr_i]):
            next_val = arrs[arr_i][next_idx]
            heapq.heappush(minheap,(next_val,arr_i,next_idx))
    return ans         
    
print(merge_k_arr2(
   [[3,5,7],
    [0,6],
    [0,6,28]
            ]))


# solution 2 time:  O(nlogn)
def merge_k_arr(arrs):
    ans = []
    for arr in arrs:
        ans.extend(arr)
    ans.sort()
    return ans
print(merge_k_arr(
   [[3,5,7],
    [0,6],
    [0,6,28]
            ]))

# solution 3
def merge_sorted_arrays(arrs: List[List[int]]) -> List[int]:
    return list(heapq.merge(*arrs))

