# 
# Your previous Plain Text content is preserved below:
# 
nums = [2,3,1,7,3,5,9]
target = 0
# 
# i :total

def total_exist(nums, target):
    total = 0
    left = 0
    for right in range(len(nums)):
        total += nums[right]
        while total > target and left < right:
            total -= nums[left]
            left += 1 
        if total == target:
            return True
    
    return False

print(total_exist(nums, target))
''' 
nums = [2,3,1,7,3,5,9]
                  r
              l
target = 15


total = 2->5-> 6 -> 13 -> 16 -> 14 -> 19 -> 16 -> 15
left = 1
right = 4
len(nums) = 7

nums[right] 


'''
# boolean
'''
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
'''
'''
[73, 74, 75, 71, 69, 72, 76, 73]
 0   1   2    3  4   5   6   7

1     1     4    2    1   1     0    0
                              
                        prev_high_idx = 6
                        highest_temp_sofar = [(76,6),(75,2),(74,1) ]
                        
array keep appending
if its empty -> 0
while its not empty and the last value from array is smaller, pop

output[1, 1, 4, 2, 1, 1, 0, 0]

'''

def find_warmer_day(T):
    ans = [0 for _ in range(len(T))]
    arr = []
    
    for i in range(len(T)-1,-1,-1):

        while arr and T[arr[-1]] <= T[i]:
            arr.pop()
            
        if arr:
            ans[i] = arr[-1] - i
        
        arr.append(i)  
    
    return ans

T = [73, 74, 75, 71, 69, 72, 76, 73]
print(find_warmer_day(T))






