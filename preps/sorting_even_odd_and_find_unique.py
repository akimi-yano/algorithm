# Find the first non-repeated char in a given String;
# input: aabbcaad;

def find_first(s):
    seen = {}
    for i,elem in enumerate(s):
        if elem not in seen:
            seen[elem]=(1,[i])
        else:
            count,arr = seen[elem]
            count+=1
            arr.append(i)
            seen[elem]=(count,arr)
        min_idx=len(s)
        min_val='_'
        for k,v in seen.items():
            c,a = v
            if c == 1 and a[0]<min_idx:
                min_idx = a[0]
                min_val  = k
    return min_val
print(find_first("aabbcaad"))



# sort an integer array in the order of all even numbers in the first half + odd second part. 
# And each part sorted in ascending order.
# in place sort
# input: int[] a = {1,2,5,6,7,3,4};
# output: a={2,4,6,1,3,5,7}
# public void sortArray(int[] arr){
# }

def sort_arr(arr):
    left, right = 0, len(arr)-1
    while left<right:
        while arr[left]%2==0: #find odd
            left+=1
        while arr[right]%2!=0: #find even
            right-=1
        if left<right:
            arr[left],arr[right]=arr[right],arr[left]
        
    odd_start = left # set odd_start to left as left is for odd
    
    # quick sort in place
    # choose a pivot (at the end of arr) and divide the arr in a way that : anything smaller - pivot - anything larger
    # keep doing that recursively until start=end 
    def divide(start,end):
        if  start>=end:
            return 
        mid = start
        for i  in range(start,end):
            if arr[i]<arr[end]:
                arr[i],arr[mid]= arr[mid],arr[i]
                mid+=1
        arr[mid],arr[end]= arr[end],arr[mid]
        divide(start,mid-1)
        divide(mid+1,end)
        
    divide(0,odd_start-1) # sort evens
    divide(odd_start,len(arr)-1) #sort odds
    return arr
print(sort_arr([1,2,5,6,7,3,4]))
print(sort_arr([1,56,3,4,5,6,7,8,10]))

