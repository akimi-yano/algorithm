# Sprinkler problem

# no zeros, no negatives
# Find minimum number of sprinklers to turn on to cover the entire array
# value of 1 covers itself and left and right neighbors
# if the sprinkler goes out of bounds that's ok
# left_bound = max(0,i - arr[i])
# right_bound = min(len(arr)-1, i + arr[i])  

# Examples:
# arr = [1,2,4,1,2] -> 1
# arr = [1,1,1,1,1] -> 2
# arr = [1,1,1,1,5] -> 1
# arr = [5,1,4,1,1] -> 1 (more than 1 solution just return first one or whatever)

import  heapq
def min_sprinkler(arr):
    max_jumps = [0]*len(arr)
    best = 0
    for i in range(len(arr)):
        best = max(best,arr[i]+i+1)
        max_jumps[i]=best
    # print(max_jumps)
    
    maxheap = []
    for k in range(len(max_jumps)-1,-1,-1):
        heapq.heappush(maxheap,((-1)*max_jumps[k],k))
        while len(maxheap)>0:
            popped = heapq.heappop(maxheap)
            val, idx = popped
            val*=(-1)
            if max_jumps[k]<val:
                if idx<=k:
                    max_jumps[k]=val
                    break
            
    print(max_jumps)        
    count = 0
    cur_i = 0
    while cur_i <len(max_jumps):
        now = max_jumps[cur_i]
        cur_i = now
        count+=1
    return count

print(min_sprinkler([1,2,4,1,2]))    
print(min_sprinkler([1,1,1,1,1]))  
print(min_sprinkler([1,1,1,1,5]))  
print(min_sprinkler([5,1,4,1,1]))  


# pseudo code 　--- 　ʕ•̼͛͡•ʕ-̺͛͡•ʔ•̮͛͡•ʔ　 ---

#   LEFT: i - arr[i]
#   RIGHT: i + arr[i]
#   every splinker is  always positive  !
#   
#        [0][1][2][3][4]
#        [1, 2, 4, 1, 2] -> 1
#1     -  -  -
#2     -  -  -  -  -      
#4  -  -  -  -  -  -  -  -  -      
#1              -  -  -    
#2              -  -  -  -  -     

# ->  self += elem is the wing span  

# 1 first path: left to right - make a table called jumps to record how far each elem can jump 
# from left to right 
# 2 second path: right to left - update the table from the right to left using max heap 