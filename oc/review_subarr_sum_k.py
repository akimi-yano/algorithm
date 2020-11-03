'''
560. Subarray Sum Equals K

https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers nums and an integer k, 
return the total number of continuous subarrays 
whose sum equals to k.

       0 1
Input:[1,1,1,2] k = 2
             ^
{
  0: 1, 1:1, 2:1, 3:1, 5:1
}
i = 0, 1, 2, 3
sum = 1, 2, 3, 5 
complement = sum - k = -1, 2-2=0, (3-2=1) (5-2=3)
k = 
count = 0, 1, 2, 3


complement = sum - k  (2-2=0)
K: prefixsum
V: frequency 
count += value (1)

- iterate thorugh the given array. 
    - running sum. 
    - count. 

  
'''

arr = [-1,1,-1,1] 
#               s
#[0,1], [2,3], [1,2]. [0,3]

k = 0
# //map.put(running_sum, map.getOrDefault(running_sum, 0) + 1);

def subarrays_sum_equal_k(nums, k): 
  running_sum = 0 
  count = 0 
  
  hash_map = {0:1}
  
  for num in nums:
    running_sum += num  
    
    complement = running_sum - k  
    print(complement)
    print(hash_map)
    # #if complement is in hash map then place that sum in the hash map   
    if complement in hash_map:
      count += hash_map[complement]
    
    if running_sum in hash_map:   
      hash_map[running_sum] +=1 
           
    else:
      hash_map[running_sum] = 1
   
  return count      
    
# print(subarrays_sum_equal_k(arr, 0))
print(subarrays_sum_equal_k([1,1,1], 2))
    