# 11.1 search a sorted array for first occurence of k
# input :
# sorted arr and a key

# r - index of the first occurence of the key 
# r -1  if you cannot find 

arr = [-14,-10,2,108,108,243,285,285,285,401] 
key = 108 #3
# key = 285 #6

# solution  !
def find_first_idx(arr,key):
    lo,hi = 0, len(arr)-1
    while lo<=hi:
        mid = (lo+hi)//2
        if arr[mid] == key and (mid==0 or arr[mid-1]!=key):
            return mid
        elif arr[mid] >= key:
            hi = mid-1
        else:
            lo = mid+1
    return  -1
        
        
print(find_first_idx(arr,key))

# another solution !
# this  approach is not to  find the answer  but to elminate all options that are not answers by divide and conquer
# it will never bypass the answer because high =  mid when arr[mid]>= key (instead of high = mid -1) 
# also  low = mid +1  when arr[mid]<key focusing on  the boundries than getting an answer

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