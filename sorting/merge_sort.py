# sorting: 

# merge sort 
# heap sort 
# quick sort 



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
print(merge_sort([3,1,4,1,5,9,2,6,5,2,5]))



# using .sort() - modifies the original arr (time: O(NlogN))
ex1 = [3,1,4,1,5,9,2,6,5,2,5]
ex1.sort()
print(ex1)

# using sorted()- make a new sorted arr (time: O(NlogN))
ex2 = [3,1,4,1,5,9,2,6,5,2,5]
new_ex2 = sorted(ex2)
print(new_ex2)

