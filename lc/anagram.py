A = [1,2,3,4]
def helper(arr):
    if len(arr) <= 1:
        return [arr]
    temp = []
    for i in range(len(arr)):
        array = helper(arr[:i]+arr[i+1:])
        for ta in array:
            temp.extend([[arr[i]]+ ta]) 
    return temp
print(helper(A))



'''
i = 0
temp = []
k 01234
array = helper(k+1)
A[k]  + arr 
r temp

i = 1
1234 
'''
