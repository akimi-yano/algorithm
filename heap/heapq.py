import heapq

def kthSmallest(arr, k):
    maxheap = []
    i = 0
    while i<k:
        heapq.heappush(maxheap,arr[i]*(-1))
        i+=1
    while i< len(arr):
        if maxheap[0]*(-1)>arr[i]:
            heapq.heappop(maxheap)
            heapq.heappush(maxheap,arr[i]*(-1))
        i+=1
    return maxheap[0]*(-1)
a = [3, 1, 4, 1, 5, 9, 2, 6, 5, 2, 5]
print(kthSmallest(a, 3))

def kthLargest(arr, k):
    minheap  = []
    i = 0
    while i < k:
        heapq.heappush(minheap, arr[i])
        i+=1
    while i<len(arr):
        if minheap[0]<arr[i]:
            heapq.heappop(minheap)
            heapq.heappush(minheap, arr[i])
        i+=1
    return minheap[0]
    
    
    

a = [3, 1, 4, 1, 5, 9, 2, 6, 5, 2, 5]
print(kthLargest(a, 3))