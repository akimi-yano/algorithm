def frequency_sorting(arr):
    memo ={}
    for num in arr:
        if num not in memo:
            memo[num]=1
        else:
            memo[num]+=1
    temp = []
    for k,v in memo.items():
        temp.append((-v,k))
    temp = sorted(temp)
    ans = []
    for elem in temp:
        count, value = elem
        count *= -1
        for _ in range(count):
            ans.append(value)
    return ans 
        

print(frequency_sorting([3,2,1,2,4,4,4,5,7, 7, 7, 7,8,8,8,8,8,8]))