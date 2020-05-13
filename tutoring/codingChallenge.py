# 1 given an unsorted array of integers, each integer is repeated twice except for one of them. 
# find and return the integer that is not duplicated
# try without constraints
# try with memory constraint -> dont use additional structures (look up bitwise)

def findUnique(arr):
    result = arr[0]
    print(bin(result))
    for i in range(1,len(arr)):
        result^=arr[i]
        print(bin(result))
    return result
print(findUnique([1,0,0,2,1]))
# print(findUnique([1,0,6,0,5,1,6]))
# print(findUnique([1,2,2,1,3,4,4,3,5,6,6,7,7]))
# a=1
# b=2
# a^=b
# print("a ^ b =",a )
# 1 = 0001
# 2 = 0010
# 0011 = 3

#2 you are provided with a number N, find the pattern given these examples:
# if n == 0: return 0
# if n == 1: return 1
# if n == 9: return 9
# if n == 10: return 19
# if n == 19: return 199
# return the correct result given the number N



#3 you are provided with a string of undetermined length. 
# it has only uppercase letters (no numbers, no special characters). 
# figure out how many times the word "BALLOON" can be extracted from the string. return the count.
def countBaloon(str):
    memo = {'B':0, 'A':0, 'L':0,'O':0,'N':0}
    for i in range(len(str)):
        if str[i] not in memo: 
            memo[str[i]]=1
        else:
            memo[str[i]]+=1
    memo['L']=memo['L']//2
    memo['O']=memo['O']//2
    return min(memo.values())
#     for key,value in memo.items():
#         print(key, value) 
# print(countBaloon('BALLOONBALLOONBALLOONBALLON'))

        

