
# 
# Your previous Plain Text content is preserved below:
# 
# /*
# 2 params: list of ints, distance
# group([1, 2, 3, 10, 22, 25, 50, 100, 101, 150], 10) -> [[1, 2, 3, 10], [22, 25], [100, 101]]
# group([1, 2, 3, 10, 15, 22, 25, 50, 100, 101, 150], 10) -> [[1, 2, 3, 10, 15, 22, 25], [100, 101]]
# group([1, 2, 3, 10, 15, 22, 25, 50, 100, 101, 150], 5) -> [([1, 2, 3] [10, 15] [22, 25] [100, 101]]]
# any numbers that aren't in group are discarded
# 
# */

'''
[1, 2, 3, 10, 22, 25, 50, 100, 101, 150], 10
              cur 

prev = None -> 1 ->2 ->3 -> 10
[1, 2, 3, 10]

None -> initialize temp arr [-1]

difference is larger than distance then
append the current array (only append if the length is larger than 1 and initialize

append 1 more time if its length is larger than 1 after the loop
ans = []

'''

def group(nums, distance):
    answer = []
    temp = []
    for num in nums:
        if temp and (num - temp[-1]) > distance:
            if len(temp) > 1:
                answer.append(temp)
            temp = []
        temp.append(num)
            
    if len(temp) > 1:
        answer.append(temp)
        
    return answer
'''
[1, 2, 3, 10, 22, 25, 50, 100, 101, 150], 10
                                    num
answer [[1, 2, 3, 10],[22, 25], [100, 101]]
temp [1, 2, 3, 10] -> [22, 25] -> [50] -> [100, 101] -> [150]


'''
print(group([1, 2, 3, 10, 22, 25, 50, 100, 101, 150], 10)) 
# [[1, 2, 3, 10], [22, 25], [100, 101]]

print(group([1, 2, 3,3, 10, 22, 25, 50, 50, 100, 101, 150, 150], 10)) 


print(group([1, 2, 3, 10, 22, 25, 50, 100, 101, 150, 154], 10)) 

# group([1, 2, 3, 10, 15, 22, 25, 50, 100, 101, 150], 10) -> [[1, 2, 3, 10, 15, 22, 25], [100, 101]]
# group([1, 2, 3, 10, 15, 22, 25, 50, 100, 101, 150], 5) -> [([1, 2, 3] [10, 15] [22, 25] [100, 101]]]
