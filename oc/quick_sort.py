    if len(arr)<2:
      return arr
    pivot = len(arr)-1
    smaller = []
    middle = []
    larger = []
  
    for num in arr:
        if num == arr[pivot]:
            middle.append(num)
        elif num < arr[pivot]:
            smaller.append(num)
        else:
            larger.append(num)
            
    sorted_smaller = quicksort(smaller) 
    sorted_larger =  quicksort(larger)
    return sorted_smaller + middle + sorted_larger