# sorting: 

# stable sort = equal items will remain in order

# inefficient sorts O(N^2) on average:
#   bubble sort: O(N^2) - stable sort - we swap my self and right enight so that myself>right - if sorted, only takes linear time complexity - constant space complexity
#   selection sort: O(N^2) - not stable sort - get the min of the right side and update onr by one as you iterate through - constant space complexity - quadratic time at best
#   insertion sort: O(N^2) - stable sort - twice faster than bubble sort and selection sort - compare each element (on the right) with already sorted portion (right) and inset the element at the right spot - constant space complexity - streamable - fast for nearly sorted arrays O(kn) where k is an average distance from the sorted position - linear time for sorted arrays - good if n<10

# more efficient sorts O(NlogN) on average:
# - more useful for larger dataset n>10
#   merge sort: O(NlogN) - stabe sort - for objects, linked lists - worst case time complexity O(NlogN) - even if its sorted, it still takes O(NlogN) time - must duplicate array so space complexity O(N)
#   heap sort: O(NlogN) -  not stable sort - worst case is still O(NlogN) - constant space complexity -  on average heap sort is slower that quick sort
#   quick sort: O(NlogN) - not stable sort - for premitives - worst case time: O(N^2) (if you choose a wrong element as pivot) but on average, quick sort is 2-3 times faster than merge sort  - even if its sorted, it still takes O(NlogN) time


# Other sorting algos:
#     Shellsort
#     Comb sort
#     Timsort - combined insertion sort and merge sort to give the best time complexity that is linear
    
import heapq

def merge_sort(arr):
    def merge(arr1,arr2):
        idx1 = 0
        idx2 = 0
        ans = []
        while idx1<len(arr1) and idx2<len(arr2):
            if arr1[idx1]<arr2[idx2]:
                ans.append(arr1[idx1])
                idx1+=1
            else:
                ans.append(arr2[idx2])
                idx2+=1
        while idx1<len(arr1):
            ans.append(arr1[idx1])
            idx1+=1
        while idx2<len(arr2):
            ans.append(arr2[idx2])
            idx2+=1
        return ans
    
    if len(arr)<2:
        return arr
    start = 0
    end = len(arr)-1
    mid = (start+end)//2
    arr1 = merge_sort(arr[start:mid+1])
    arr2 = merge_sort(arr[mid+1:end+1])
    return merge(arr1,arr2)
# using merge sort (time: O(NlogN))
print("merge sort: ",merge_sort([3,1,4,1,5,9,2,6,5,2,5]))



# using .sort() - modifies the original arr (time: O(NlogN))
ex1 = [3,1,4,1,5,9,2,6,5,2,5]
ex1.sort()
print(".sort(): ",ex1)

# using sorted() - make a new sorted arr (time: O(NlogN))
ex2 = [3,1,4,1,5,9,2,6,5,2,5]
new_ex2 = sorted(ex2)
print("sorted: ",new_ex2)

# using heapsort (time: O(NlogN))
def heap_sort(arr):
    minheap = []
    ans = []
    for num in arr:
        heapq.heappush(minheap,num)
    while len(minheap)>0:
        popped = heapq.heappop(minheap)
        ans.append(popped)
    return ans

print("heap sort: ", heap_sort([3,1,4,1,5,9,2,6,5,2,5]))


# using quick sort 
# 1 choose a middle element based on the length of arr
# 2 smaller values to left arr and larger values to right arr if same as the middle one, middle arr
# 3 put together the 3 arrs at the end

# input arr
# separate the arr into three pieces
# return arr thats put together


# do in place version later to optimize it
def quick_sort(arr):
    if len(arr)<2:
        return arr
    pivot = arr[len(arr)//2]
    left = []
    right = []
    middle = []
    for elem in arr:
        if elem==pivot:
            middle.append(elem)
        elif elem<pivot:
            left.append(elem)
        else:
            right.append(elem)
    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)

    return sorted_left + middle + sorted_right

print("quick sort: ", quick_sort([3,1,4,1,5,9,2,6,5,2,5]))